import telebot
from .models import *
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages


TELEGRAM_BOT_TOKEN = '7445289117:AAEda8GqhWqa8enFFPBgal9dl8wdYvcnms8'
TELEGRAM_CHAT_ID = '-1002550303976'

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

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
        
        try:
            # Форматируем красивое сообщение
            message = f"""📝 <b>Новая заявка на визу в США</b>
            
👤 <b>Контактная информация:</b>
🆔 Имя: {name}
📩 Email: {email}
💬 Комментарий: {comment}"""
            
            # Отправляем сообщение с HTML разметкой
            bot.send_message(
                chat_id=TELEGRAM_CHAT_ID,
                text=message,
                parse_mode='HTML'
            )
            
        except Exception as e:
            print(f"Ошибка отправки в Telegram: {e}")
            return False
     
        messages.success(request, "Спасибо! Ваше сообщение отправлено.")
        return redirect(request.META.get('HTTP_REFERER', '/'))
    else:
        return render(request, 'mainapp/application.html')


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
        try:
            # Форматируем красивое сообщение
            message = f"""
            📝 <b>Новая заявка на визу в США</b>

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
            
            # Отправляем сообщение с HTML разметкой
            bot.send_message(
                chat_id=TELEGRAM_CHAT_ID,
                text=message,
                parse_mode='HTML'
            )
            
        except Exception as e:
            print(f"Ошибка отправки в Telegram: {e}")
            return False
        
        
        
        return redirect('mainapp:index') 
    else:
        return render(request, 'mainapp/application.html')