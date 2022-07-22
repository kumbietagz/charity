from django.shortcuts import render
from django.contrib.auth.models import User, Permission
from .models import Sponsor, Student, Assessor, Fund, Message
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import permission_required
from django.db.models import Avg, Count, Sum
from django.db.models import IntegerField
from datetime import datetime as d
from django.utils.dateparse import parse_date
import joblib
from django.db.models import Q

forest_job = joblib.load('ML/randForest.pkl')


# Create your views here.

def search_student(request):
    query = request.GET["q"]
    search = Student.objects.filter(Q(first_name__icontains=query)|Q(last_name__icontains=query)|Q(forest__icontains=query) | Q(approval__icontains=query)  )
    return render(request, "donate/student_search.html", {"search":search})

def search_sponsor(request):
    query = request.GET["q"]
    search = Sponsor.objects.filter(Q(first_name__icontains=query)|Q(last_name__icontains=query)|Q(address__icontains=query) | Q(city__icontains=query) | Q(country__icontains=query)  )
    return render(request, "donate/sponsor_search.html", {"search":search})
    


def search_message(request):
    query = request.GET["q"]
    search = Message.objects.filter(Q(name__icontains=query)|Q(text__icontains=query)  )
    return render(request, "donate/message_search.html", {"search":search})

@permission_required('donate.assessor', login_url='donate:assessor-login')
def messages(request):
    messages = Message.objects.all()
    return render(request, 'donate/message.html', {'messages':messages})

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

def assessor_login(request):
    message = ""
    if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            message = "Incorrect username or password."
            if user is not None and user.has_perm('donate.assessor'):
                login(request, user)
                return HttpResponseRedirect(reverse("donate:students"))
            return render(request, "donate/assessor_login.html", {"message":message})
    return render(request, "donate/assessor_login.html", {"message":message})


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

@permission_required('donate.assessor', login_url='donate:assessor-login')
def sponsor_detail(request, id):
    sponsor = Sponsor.objects.get(id = id)
    return render(request, 'donate/sponsor_detail.html', {'sponsor':sponsor}) 

def index(request):
    students = Student.objects.filter(approval="Approved")
    sponsors = Sponsor.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        message = Message.objects.create(name = name, email=email, text=text)
        message.save()
    return render(request, 'donate/index.html', {'students':students, 'sponsors':sponsors})
    

def about(request):
    return render(request, 'donate/about.html')

@permission_required('donate.sponsor', login_url='donate:sponsor-login')
def sponsor(request):
    sponsor = Sponsor.objects.get(user=request.user)
    if request.method == 'POST':
        sponsor.first_name = request.POST['first']
        sponsor.last_name = request.POST['last']
        sponsor.email = request.POST['email']
        sponsor.phone = request.POST['phone']
        sponsor.dob = request.POST['dob']
        sponsor.address = request.POST['address']
        sponsor.city = request.POST['city']
        sponsor.country = request.POST['country']      
           
        for key in request.FILES:
            if key == "image":
                student.image = request.FILES["image"]
        
    return render(request, 'donate/sponsor.html', {'sponsor':sponsor})


def login_register(request):
    return render(request, 'donate/login_register.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        message = Message.objects.create(name = name, email=email, text=text)
        message.save()
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
        student.age = age

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

        if forest_pred == 'Fund Worthy':
            forest_con = forest_job.predict_proba([[student.gender, age, student.feesav, student.dhav, student.health, student.residence]])[0][1]
            
            student.confidence = forest_con*100
        else:
            forest_con = forest_job.predict_proba([[student.gender, age, student.feesav, student.dhav, student.health, student.residence]])[0][0]
            student.confidence = forest_con*100

        student.save()
    return render(request, 'donate/student.html', {"student":student})

@permission_required('donate.sponsor', login_url='donate:sponsor-login')
def fund(request, id):
    student = Student.objects.get(id=id)
    sponsor = Sponsor.objects.get(user=request.user)
    if request.method == 'POST':
        
        amount = request.POST['amount']
        fund = Fund.objects.create(sponsor=sponsor, student=student, amount=amount)     
    amount_sum = Fund.objects.filter(student = student).aggregate( Sum('amount', output_field=IntegerField()))
    student.crowdfund = amount_sum['amount__sum']
    student.progress = (student.crowdfund/student.fees)*100
    if student.progress > 100:
        student.progress = 100

    student.save()

    print(amount_sum['amount__sum'])

    print(student.crowdfund)


    return render(request, 'donate/fund.html')

@permission_required('donate.assessor', login_url='donate:assessor-login')
def students(request):
    students = Student.objects.all()
    return render(request, 'donate/students.html', {'students':students})

def stud_detail(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'donate/stud_detail.html', {'student':student})

def spons_detail(request, id):
    sponsor = Sponsor.objects.get(id=id)
    return render(request, 'donate/spons_detail.html', {'sponsor':sponsor})

@permission_required('donate.assessor', login_url='donate:assessor-login')
def sponsors(request):
    sponsors = Sponsor.objects.all()
        
    return render(request, 'donate/sponsors.html', {'sponsors':sponsors})

def student_detail(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.approval = request.POST['approval']
        student.save()
    return render(request, 'donate/student_detail.html', {'student':student})

@permission_required('donate.assessor', login_url='donate:assessor-login')
def assessor(request):
    students = Student.objects.all()
    return render(request, 'donate/students.html', {'students':students})


@permission_required('donate.sponsor', login_url='donate:sponsor-login')
def donations(request):
    sponsor = Sponsor.objects.get(user = request.user)
    donations = Fund.objects.filter(sponsor = sponsor)
    return render(request, 'donate/donations.html', {'donations':donations})

@permission_required('donate.student', login_url='donate:student-login')
def funds(request):
    student = Student.objects.get(user = request.user)
    funds = Fund.objects.filter(student = student)
    return render(request, 'donate/funds.html', {'funds':funds})

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
    return render(request, "donate/assessor_login.html",{
        "message": "Logged out",
    })