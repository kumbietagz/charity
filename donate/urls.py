from django.urls import path
from . import views

app_name='donate'
urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('sponsor', views.sponsor, name='sponsor'),
    path('login_register', views.login_register, name='login-register'),
    path('contact', views.contact, name='contact'),
    path('student', views.student, name='student'),
        
    ]