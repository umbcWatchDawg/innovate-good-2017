from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout
from . import models
from django.forms import Form
import datetime

def index(request):
    isAuth = request.user.is_authenticated
    if isAuth:
        return report(request)
    else:
        return render(request, 'watchdawg/signIn.html')

def about(request):
    return render(request, 'watchdawg/about.html', {'path': 'about'})

def contact(request):
    return render(request, 'watchdawg/contact.html', {'path': 'contact'})

def login(request):
    return render(request, 'watchdawg/signIn.html')

# sends a GET to go to victim_wintness
def report(request):
    return render(request, 'watchdawg/report.html')

# step 1, sends POST to crime_type with victim or witness
def victim_witness(request):
    crime_obj = models.Crime(user_key=request.user,date=datetime.now())
    crime_obj.save()
    obj_id = getattr(crime_obj, 'id')
    return render(request, 'watchdawg/vicWit.html', {'id': obj_id})

#step 2
def crime_type(request):
    if request.method == 'POST':
        form = Form(request.POST)


    return render(request, 'watchdawg/typeCrime.html')

def elements(request):
    return render(request, 'watchdawg/elements.html')

def questions(request):
    return render(request, 'watchdawg/questions.html')
