from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages






def index(request):
    template = "mainapp/index.html"
    return render(request, template)

def application(request):
    template = "mainapp/application.html"
    return render(request, template)

def feedback_footer(request):
    if request.method == 'POST':
        name_value = request.POST.get('name')
        email_value = request.POST.get('email')
        message_value = request.POST.get('message')
        print("name_value", name_value)
        messages.success(request, "Спасибо! Ваше сообщение отправлено.")
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return render(request, 'mainapp/application.html')


def feedback_application(request):
    if request.method == 'POST':
        name_value = request.POST.get('name')
        email_value = request.POST.get('email')
        message_value = request.POST.get('message')
        print("name_value", name_value)
        return redirect('mainapp:index') 
    else:
        return render(request, 'mainapp/application.html')