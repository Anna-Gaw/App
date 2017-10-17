from django import forms
from django.core.validators import EmailValidator


class UserLoginForm(forms.Form):
    username = forms.CharField(label = 'Username')  #, widget= forms.EmailInput) 
    password= forms.CharField(label = 'Hasło', widget= forms.PasswordInput)
    
class NewUserForm(forms.Form):
    username = forms.CharField(label = 'Nick')
    first_name = forms.CharField(label= 'Imie')
    last_name = forms.CharField(label = 'Nazwisko')
    email = forms.CharField(label = 'Email', validators= [EmailValidator()])
    birth_date = forms.DateField(label = 'Data urodzenia')
    password = forms.CharField(widget=forms.PasswordInput())
    password_2=  forms.CharField(widget=forms.PasswordInput())
    