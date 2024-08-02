from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
View is a request handler.
'''

def home(request):
    #return HttpResponse("Home Page")
    return render(request,'index.html')

def say_Hi(request):
    return HttpResponse('Hi')
