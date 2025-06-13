import telebot
from .models import *
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils import translation
from django.urls import translate_url
from django.conf import settings



TELEGRAM_BOT_TOKEN = '7445289117:AAEda8GqhWqa8enFFPBgal9dl8wdYvcnms8'
TELEGRAM_CHAT_ID = '-1002550303976'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

def change_language(request, lang_code):
    translation.activate(lang_code)
    request.session[settings.LANGUAGE_COOKIE_NAME] = lang_code
    return redirect('mainapp:index')


def index(request):
    template = "mainapp/index.html"
    return render(request, template)

def application(request):
    template = "mainapp/application.html"
    return render(request, template)

def feedback_footer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('message')
        from_email='shakhnoza.yuldasheva@samarkand-zakovat.uz' 
        recipient = 'info@samarkand-zakovat.com'
        subject = 'Новое сообщение с формы обратной связи'
        message = f"""📝 <b>Новая заявка на визу в США</b>
            
👤 <b>Контактная информация:</b>
🆔 Имя: {name}
📩 Email: {email}
💬 Комментарий: {comment}"""

        
        try:
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode='HTML')
        except Exception as e: return redirect(request.META.get('HTTP_REFERER', '/'))
        
        try:
            send_mail(subject=subject, message=message, from_email=from_email, 
                      recipient_list=[recipient], fail_silently=False)
        except Exception as e: return redirect(request.META.get('HTTP_REFERER', '/'))
        
        messages.success(request, "Спасибо! Ваше сообщение отправлено.")
        return redirect(request.META.get('HTTP_REFERER', '/'))
    


def feedback_application(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        telegram = request.POST.get('telegram')
        age = request.POST.get('age')
        nation = request.POST.get('nation')
        inst = request.POST.get('inst')
        work = request.POST.get('work')
        money = request.POST.get('money')
        countries = request.POST.get('countries')
        trip_purpose = request.POST.get('trip_purpose') 
        visa_history = request.POST.get('visa')
        travel_companions = request.POST.get('count_people')
        relatives_in_usa = request.POST.get('relatives')
        visa_refusals = request.POST.get('refusals')
        city = request.POST.get('my_city')
        from_email='shakhnoza.yuldasheva@samarkand-zakovat.uz'
        recipient = 'info@samarkand-zakovat.com'
        subject = 'Новое сообщение с формы обратной связи'
        message = f"""📝 <b>Новая заявка на визу в США</b>

👤 <b>Контактная информация:</b>
✅ Имя: {name}
✅ Email: {email}
✅ Телефон: {phone}
✅ Telegram: @{telegram}

🏠 <b>Личные данные:</b>
✅ Возраст: {age}
✅ Гражданство: {nation}
✅ Город проживания: {city}

💼 <b>Профессиональная информация:</b>
✅ Сфера деятельности: {work}
✅ Примерный доход: {money}

🌎 <b>Информация о поездке:</b>
✅ Цель поездки: {trip_purpose}
✅ Посещенные страны: {countries}
✅ История виз США: {visa_history}

👨‍👩‍👧‍👦 <b>Дополнительная информация:</b>
✅ Спутники: {travel_companions}
✅ Родственники в США: {relatives_in_usa}
✅ Отказы в визах: {visa_refusals}

📱 <b>Соцсети:</b>
✅ Instagram: {inst}
            """
        try:
            bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message, parse_mode='HTML')
        except Exception as e: return redirect('mainapp:index') 
        
        try:
            send_mail(subject=subject, message=message, from_email=from_email, 
                      recipient_list=[recipient], fail_silently=False)
        except Exception as e: return redirect(request.META.get('HTTP_REFERER', '/'))
            
        return redirect('mainapp:index') 


