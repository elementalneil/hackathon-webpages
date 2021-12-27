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
    #Time Calculation Starts Here:
    event_time=1641389400.0
    current_time=time.time()

    rem_time=int(event_time-current_time)

    days=rem_time//86400
    rem_time=rem_time%86400
    hours=rem_time//3600
    rem_time=rem_time%3600
    minutes=rem_time//60
    seconds=rem_time%60
    time_dict={'days': days, 'hours': hours, 'minutes': minutes, 'seconds': seconds}
    #Time Calculated and Stored

    context={'participants':participants, 'time':time_dict}
    return render(request, 'base/home.html', context)

def contact(request):
    return render(request, 'base/contact.html')