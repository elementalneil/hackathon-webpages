from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('You are in Home Page')

def contact(request):
    return HttpResponse('You are in Contact Us Page')