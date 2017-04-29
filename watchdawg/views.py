from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    isAuth = request.user.is_authenticated
    if isAuth:
        return report(request)
    else:
        return HttpResponse("Hello, world. You've reached watchdawg!")

def login(request):
    return render(request, 'watchdawg/login.html')

@login_required
def logout(request):
    return index(request)

@login_required
def report(request):
    return render(request, 'watchdawg/report.html')
