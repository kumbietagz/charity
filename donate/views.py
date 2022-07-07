from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'donate/index.html')
    

def about(request):
    return render(request, 'donate/about.html')

def sponsor(request):
    return render(request, 'donate/sponsor.html')

def login_register(request):
    return render(request, 'donate/login_register.html')

def contact(request):
    return render(request, 'donate/contact.html')

def student(request):
    return render(request, 'donate/student.html')
