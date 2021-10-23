from django.http.response import HttpResponse
from django.shortcuts import render
from cycleapp import models

# Create your views here.

def home(request):
    home_obj = models.Home.objects.first()
    context = {
        'obj' : home_obj
    }
    

    return render(request ,'cycleapp/home.html' , context=context)




