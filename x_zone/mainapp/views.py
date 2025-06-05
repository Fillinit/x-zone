from .models import *
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt



def index(request):
    template = "mainapp/index.html"
    return render(request, template)

def application(request):
    template = "mainapp/application.html"
    return render(request, template)

    

