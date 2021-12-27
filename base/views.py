from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
participants=[                      #Temporary Context
    {'id':1, 'name':'John Doe'},
    {'id':2, 'name':'Jane Doe'},
    {'id':3, 'name':'Jack Doe'},
]

def home(request):
    context={'participants':participants}
    return render(request, 'base/home.html', context)

def contact(request):
    return render(request, 'base/contact.html')