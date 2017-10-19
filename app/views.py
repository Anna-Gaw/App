from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import UserLoginForm, NewUserForm, MessageForm
from django.views.generic.edit import CreateView
from .models import Customer, Food, Message,Order,Bonus
from django.contrib.auth.hashers import make_password
from django.views.generic.detail import DetailView
from django.http import HttpRequest
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class BaseView(View):
    def get(self, request):           
        return render(request, "base.html")
    
class UserLoginView(View): 
    def get(self, request):  
        form = UserLoginForm()
        return render(request, 'user_login.html',  {'form': form})
    
    def post(self,request):
        form  = UserLoginForm(request.POST)
        if form.is_valid(): 
#             import pdb ; pdb.set_trace()
            user = authenticate( 
                username =form.cleaned_data['username'], 
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('my_message'))   
            else:
                form.add_error(None, 'Niepoprawne dane logowania...')
                return render(request, 'user_login.html',  {'form': form})
                
            
            
            
class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))   
    
    
class NewUserView(View):

    def get(self, request):
        form = NewUserForm()
        return  render(request, 'new_user.html', {'form': form})
        
        
    def post (self, request):
        form= NewUserForm(request.POST)
        if form.is_valid():
            username =form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name'] 
            email = form.cleaned_data['email']
            birth_date = form.cleaned_data['birth_date']
            password =form.cleaned_data['password']
            new_user = Customer.objects.create(
                username = username,
                first_name = first_name,
                last_name = last_name,
                email= email,
                birth_date=birth_date,
                password= make_password(password,hasher='pbkdf2_sha256')
            )
            url = reverse('login', kwargs={'user_id': new_user.id})
            return HttpResponseRedirect(url)
        else:
            return render(request, 'new_user.html', {'form': form})  
                        

class CustomerDetailView(DetailView): 
    def get (self, request, user_id):
        customers = Customer.objects.get(id=user_id)
        ctx ={ 
            'customers' : customers,
        }
        return render (request, "customer_detail.html", ctx)
    
#    (1, 'Przystawki'),
#    (2, 'Zupy'),
#    (3, 'Dania główne'),
##    (4, 'Dodatki'),
#    (5, 'Desery'),
#    (6, 'napoje')
class OrderView(LoginRequiredMixin, DetailView):
    def get(self, request):
        Przystawki = Food.objects.filter(type=1)
        Zupy = Food.objects.filter(type=2)
        Dania = Food.objects.filter(type=3)
        Dodatki = Food.objects.filter(type=4)
        Desery = Food.objects.filter(type=5)
        Napoje = Food.objects.filter(type=6)
        
        ctx ={
            'Przystawki': Przystawki,
            'Zupy': Zupy,
            'Dania': Dania,
            'Dodatki': Dodatki,
            'Desery': Desery,
            'Napoje': Napoje,
            
            }
        return  render(request, 'order.html', ctx)
    def post(self,request):
        foods = Food.objects.all() 
        suma_zamowien=0
        ilosc_zamowien=0
        for food in foods:
            #food_obj=Food.objects.get(id=food.id)  
            quantity=request.POST[str(food.id)] # Poniewaz w order.html mamy nazwe pola name="{{ f.id }}"
            new_Order = Order.objects.create(
                customer = request.user,
                quantity= quantity,
                food = food,
            )
            quant=int(quantity)
            ilosc_zamowien=ilosc_zamowien+1
            suma_zamowien=suma_zamowien+(quant*int(food.price))
            new_Order.save()
        if(suma_zamowien>300 and suma_zamowien <= 500):
            new_Bonus=Bonus.objects.create(
                customer=request.user,
                text="10% rabatu do wykorzystania w lokalu",
                
                )
            new_Bonus.save()
        url = reverse('order_list')
        if (suma_zamowien > 500):
            new_Bonus=Bonus.objects.create(
                customer=request.user,
                text = "15% zniżki na dania głowne do wykorzystania  w lokalu",
                )
            new_Bonus.save()
        return HttpResponseRedirect(url)
#         return  render(request, 'order.html', None) 
class OrderListView(LoginRequiredMixin, DetailView):
    def get (self, request):
#         orders = Order.objects.order_by('-creation_date').all()
        orders = Order.objects.order_by('-creation_date').filter(customer = request.user)
        suma_zamowien=0
        ilosc_zamowien=0
        
        for order in orders:
            quant=int(order.quantity)
            ilosc_zamowien=ilosc_zamowien+1
            suma_zamowien=suma_zamowien+(quant*order.food.price)
            
        ctx = { 
            'orders' : orders,
            'suma_zamowien':suma_zamowien,
            'ilosc_zamowien':ilosc_zamowien,
            
        }
        return render(request, 'order_list.html', ctx)
        
        
class MessageView(LoginRequiredMixin, View):
    def get(self, request):
        form = MessageForm()
        return  render(request, 'message.html', {'form': form})
        
        
    def post (self, request):
        form= MessageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            customer = request.user    
            new_massage = Message.objects.create(
                title = title,
                text= text,
                customer = customer,
            )
            url = reverse('my_message')
            return HttpResponseRedirect(url)
        else:
            return render(request, 'message.html', {'form': form})  
        
   
class MyMessageView(LoginRequiredMixin, View):
    def get (self, request):
        texts = Message.objects.order_by('-creation_date').filter(customer = request.user)

        ctx ={ 
            'texts' : texts,
            
        }
        return render (request, "all_message.html", ctx)
    
    
class GetMessageView(LoginRequiredMixin, View):
    def get (self, request):
        orders = Order.objects.order_by('-creation_date').filter(customer = request.user)
        promocje=Bonus.objects.order_by('-creation_date').filter(customer=request.user)
             
        ctx={
            "promocje":promocje,
        }
         
        return render (request, "get_message.html",ctx)
      
   
   
   