from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('application/', views.application, name='application'),
    path('feedback/footer', views.feedback_footer, name='feedback_footer'),
    path('feedback/application', views.feedback_application, name='feedback_application'),
]
