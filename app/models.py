from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Create your models here.

 
class Customer(AbstractUser):
    birth_date = models.DateField(null=True, blank=True)

    
kind_of_food = (
    (1, 'Przystawki'),
    (2, 'Zupy'),
    (3, 'Dania główne'),
    (4, 'Dodatki'),
    (5, 'Desery'),
    (6, 'napoje')
)
    
class Food(models.Model):
    name = models.CharField(max_length=256)
    quantity = models.IntegerField(null = True)
    price = models.IntegerField(default=0)
    type = models.IntegerField(choices=kind_of_food, default= 1)
    customer = models.ManyToManyField(Customer)
    
    
    