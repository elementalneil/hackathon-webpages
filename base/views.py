from django.shortcuts import render
from django.http import HttpResponse
from .models import Participant
from .forms import ParticipantForm
from django.shortcuts import render, redirect

# Create your views here.
# participants=[                      #Temporary Context
#     {'id':1, 'name':'John Doe'},
#     {'id':2, 'name':'Jane Doe'},
#     {'id':3, 'name':'Jack Doe'},
# ]

def home(request):
    participants = Participant.objects.all()
    context={'participants':participants}
    return render(request, 'base/home.html', context)

def contact(request):
    return render(request, 'base/contact.html')

def register(request):
    form = ParticipantForm()

    # p=Participant(name='JD', dob='1997-01-01', roll='M156487CA', branch='BTech', mobile='+911546567251', email='jd@gmail.com', sex='F')
    # p.save()
    if request.method == 'POST':
        p=Participant()
        p.name=request.POST.get('name')
        p.dob=request.POST.get('dob')
        p.roll=request.POST.get('roll')
        p.branch=request.POST.get('branch')
        p.mobile=request.POST.get('mobile')
        p.email=request.POST.get('email')
        p.sex=request.POST.get('sex')
        p.save()
        return redirect('home')
    #     # form = ParticipantForm(request.POST)
    #     # if form.is_valid():
    #     #     form.save()

    return render(request, 'base/form.html')