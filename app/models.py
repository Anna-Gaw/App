from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

 
class Customer(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.username
    
kind_of_food = (
    (1, 'Przystawki'),
    (2, 'Zupy'),
    (3, 'Dania główne'),
    (4, 'Dodatki'),
    (5, 'Desery'),
    (6, 'Napoje')
)
    
class Food(models.Model):
    name = models.CharField(max_length=256)
    price = models.IntegerField(default=0)
    type = models.IntegerField(choices=kind_of_food, default= 1)
#     customer = models.ManyToManyField(Customer,  blank=True, )

    def __str__(self):
        return self.name+"; CENA:"+str(self.price)
    
class Message(models.Model):
    title = models.CharField(max_length = 125)
    text = models.TextField(max_length=50000)
    creation_date = models.DateTimeField(auto_now_add =True)
    customer = models.ForeignKey(Customer)
    
class Order(models.Model):
    customer = models.ForeignKey(Customer)
    food = models.ForeignKey(Food)
    quantity = models.IntegerField(null = True, blank=True , default= 1)
    creation_date = models.DateTimeField(auto_now_add =True)
#     SELECT sql FROM sqlite_master WHERE tbl_name = 'app_food_customer' AND type = 'table'
    
    
class Bonus(models.Model):  
    customer = models.ForeignKey(Customer)
    text = models.TextField(max_length=50000)
    creation_date = models.DateTimeField(auto_now_add =True)
    