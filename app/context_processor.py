import datetime
from .models import Customer

def base(request):
    
    ctx ={
        'date' : datetime.date.today(),
        'user_id' : request.user.id,
        }
    return ctx