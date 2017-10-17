from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import UserLoginForm, NewUserForm
from django.views.generic.edit import CreateView
from .models import Customer, Food
from django.views.generic.detail import DetailView
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
                return HttpResponseRedirect(reverse('detale'))   
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
                password= password,
            )
            url = reverse('detale', kwargs={'user_id': new_user.id})
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
    

class OrderView(DetailView):
    def get(self, request):
        food = Food.objects.all()
        ctx ={
            'food': food,
            }
        return  render(request, 'order.html', ctx)
        
   