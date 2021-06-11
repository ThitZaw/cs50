from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    today = datetime.now()
    values = {
        "newyear": datetime.now().day == 1 and datetime.month == 1
    }
    return render(request,"newyear/index.html",values)