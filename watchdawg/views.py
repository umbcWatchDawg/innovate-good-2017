from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

def index(request):
    isAuth = request.user.is_authenticated
    if isAuth:
        return report(request)
    else:
        return render(request, 'watchdawg/signIn.html')

def about(request):
    return render(request, 'watchdawg/about.html')

def contact(request):
    return render(request, 'watchdawg/contact.html')

def login(request):
    return render(request, 'watchdawg/signIn.html')

def report(request):
    return render(request, 'watchdawg/report.html')

def victim_witness(request):
    return render(request, 'watchdawg/vicWit.html')

def crime_type(request):
    return render(request, 'watchdawg/typeCrime')
