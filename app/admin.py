from django.contrib import admin
from .models import Customer, Food

# Register your models here.
class CustomerFoodInlineAdmin(admin.TabularInline):
    model = Food.customer.through
     
 
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    exclude = ('last_login_0', 'last_login_1')
    inlines = (CustomerFoodInlineAdmin,)
    

@admin.register(Food)    
class FoodAdmin(admin.ModelAdmin):
    list_display= ('name', 'type', 'price')
    inlines = (CustomerFoodInlineAdmin,)