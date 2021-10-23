from django.http.response import HttpResponse
from django.shortcuts import render
from cycleapp import models
import imgkit
from django.utils.encoding import smart_str
import numpy as np
import requests , cv2
from django import template

# Create your views here.

def home(request):
    home_obj = models.Home.objects.first()
    context = {
        'obj' : home_obj
    }
    

    return render(request ,'cycleapp/home.html' , context=context)


def url():
    resp = requests.get('https://www.geeksforgeeks.org/imagefield-django-models')
    image = np.asarray(bytearray(resp.content) , dtype='uint8')
    image = cv2.imdecode(image , cv2.IMREAD_COLOR)
    cv2.imwrite('out.png' , image)


def htciapi(html):
    HCTI_API_ENDPOINT = "https://hcti.io/v1/image"
    HCTI_API_USER_ID = '2f523b47-5f55-42e5-967b-c8856d73e249'
    HCTI_API_KEY = '2ca6f00f-2de9-491e-815c-3843b000dd83'

    data = html

    image = requests.post(url = HCTI_API_ENDPOINT, data = 'https://www.geeksforgeeks.org/imagefield-django-models/', auth=(HCTI_API_USER_ID, HCTI_API_KEY))
    print('*'*50)
    print(image.json())
    print("Your image URL is: %s"%image.json()['url'])
    return image.json()['url']


