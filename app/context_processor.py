import datetime
from .models import Customer

def base(request):
    
    ctx ={
        'date' : datetime.date.today(),
        }
    return ctx