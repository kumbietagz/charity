from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Sponsor, Student, Assessor, Fund
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import permission_required
from datetime import datetime as d
from django.utils.dateparse import parse_date
import joblib
forest_job = joblib.load('ML/randForest.pkl')


# Create your views here.

def student_login(request):
    message = ""
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            message = "Incorrect username or password."
            if user is not None and user.has_perm('donate.student'):
                student = Student.objects.get(user = user)
                login(request, user)
                return HttpResponseRedirect(reverse("donate:student"))
            return render(request, "donate/student_login.html", {"message":message})
    return render(request, "donate/student_login.html", {"message":message})

def sponsor_login(request):
    message = ""
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            message = "Incorrect username or password."
            if user is not None and user.has_perm('donate.sponsor'):
                sponsor = Sponsor.objects.get(user = user)
                login(request, user)
                return HttpResponseRedirect(reverse("donate:sponsor"))
            return render(request, "donate/sponsor_login.html", {"message":message})
    return render(request, "donate/sponsor_login.html", {"message":message})

def student_register(request):
    message = ""
    if request.method == "POST":
        first = request.POST["first"]
        last = request.POST["last"]
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        #user = User.objects.get(username=username)
        if True:
            if password == repassword:
                new_user = User.objects.create_user(username, password=password)             
                student = Student.objects.create(user = new_user, first_name=first, last_name=last, email=email, phone=phone) 
                student.save()
                new_user.save()
                permission = Permission.objects.get(codename='student')
                new_user.user_permissions.add(permission)
                login(request, new_user)
                return HttpResponseRedirect(reverse("donate:student"))
            message="Passwords do not match."
            return render(request, "photos/student_register.html", {"message":message})  
        message="User already exists."
    return render(request, "donate/student_register.html", {"message":message})

def sponsor_register(request):
    message = ""
    if request.method == "POST":
        first = request.POST["first"]
        last = request.POST["last"]
        username = request.POST["username"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        #user = User.objects.get(username=username)
        if True:
            if password == repassword:
                new_user = User.objects.create_user(username, password=password)             
                sponsor = Sponsor.objects.create(user = new_user, first_name=first, last_name=last, email=email, phone=phone) 
                sponsor.save()
                new_user.save()
                permission = Permission.objects.get(codename='sponsor')
                new_user.user_permissions.add(permission)
                login(request, new_user)
                return HttpResponseRedirect(reverse("donate:sponsor"))
            message="Passwords do not match."
            return render(request, "photos/sponsor_register.html", {"message":message})  
        message="User already exists."
    return render(request, "donate/sponsor_register.html", {"message":message})

def assess(request, id):
    return render(request, 'donate/assess.html')

def sponsor_detail(request, id):
    return render(request, 'donate/sponsor_detail.html')

def index(request):
    return render(request, 'donate/index.html')
    

def about(request):
    return render(request, 'donate/about.html')

@permission_required('donate.sponsor', login_url='donate:sponsor-login')
def sponsor(request):
    return render(request, 'donate/sponsor.html')

def login_register(request):
    return render(request, 'donate/login_register.html')

def contact(request):
    return render(request, 'donate/contact.html')


# student view
@permission_required('donate.student', login_url='donate:student-login')
def student(request):
    student = Student.objects.get(user=request.user)
    date = d.now()

    if request.method == 'POST':
        student.first_name = request.POST['first']
        student.last_name = request.POST['last']
        student.email = request.POST['email']
        student.phone = request.POST['phone']
        student.dob = request.POST['dob']
        student.address = request.POST['address']
        student.city = request.POST['city']
        student.country = request.POST['country']
        student.gender = request.POST['gender']
        student.residence = request.POST['residence']
        student.feesav = request.POST['feesav']
        student.dhav = request.POST['dhav']
        student.health = request.POST['health']
        student.fees = request.POST['fees']
        student.feesdue = request.POST['feesdue']
        student.institute = request.POST['institute']
        student.program = request.POST['program']
        student.about = request.POST['about']
        age = date.year - parse_date(student.dob).year 

        # classify student with presaved random forest model
        forest_pred = forest_job.predict([[student.gender, age, student.feesav, student.dhav, student.health, student.residence]])[0]
        if forest_pred == 1:
            forest_pred = "Fund Worthy"
        else:
            forest_pred = "Not Qualify"

        student.forest = forest_pred
        
        for key in request.FILES:
            if key == "image":
                student.image = request.FILES["image"]

        if trees_pred and forest_pred == 1:
            forest_con = forest_job.predict_proba([[student.gender, age, student.feesav, student.dhav, student.health, student.residence]])[0][1]
            student.confidence = forest_con*100
        else:
            forest_con = forest_job.predict_proba([[student.gender, age, student.feesav, student.dhav, student.health, student.residence]])[0][0]
            student.confidence = forest_con*100

        student.save()

    return render(request, 'donate/student.html', {"student":student})

def fund(request, id):
    return render(request, 'donate/fund.html')

def students(request):
    return render(request, 'donate/students.html')

def sponsors(request):
    return render(request, 'donate/students.html')

def student_detail(request, id):
    return render(request, 'donate/student_detail.html')

def assessor(request):
    return render(request, 'donate/assessor.html')

def donations(request):
    return render(request, 'donate/donations.html')

def funds(request):
    return render(request, 'donate/funds.html')

def search(request, k):
    return render(request, 'donate/search.html')

def student_logout(request):
    logout(request)
    return render(request, "donate/student_login.html", {
        "message": "Logged out.",
    })

def sponsor_logout(request):
    logout(request)
    return render(request, "donate/sponsor_login.html", {
        "message": "Logged out.",
    })

def assessor_logout(request):
    logout(request)
    return render(request, "donate/login.html",{
        "message": "Logged out",
    })