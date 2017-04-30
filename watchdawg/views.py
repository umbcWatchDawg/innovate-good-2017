from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def index(request):
    isAuth = request.user.is_authenticated
    if isAuth:
        return report(request)
    else:
        return render(request, 'watchdawg/signin.html')

def login(request):
    return render(request, 'watchdawg/signin.html')

#@login_required
def report(request):
    return render(request, 'watchdawg/report.html')
