from django.urls import path
from . import views

app_name='donate'
urlpatterns = [
    path('', views.index, name='index'),
    path('student_register', views.student_register, name='student-register'),
    path('sponsor_register', views.sponsor_register, name='sponsor-register'),
    path('student_login', views.student_login, name='student-login'),
    path('sponsor_login', views.sponsor_login, name='sponsor-login'),
    path('about', views.about, name='about'),
    path('sponsor', views.sponsor, name='sponsor'),
    path('register', views.student_register, name='register'),
    path('login_register', views.login_register, name='login-register'),
    path('contact', views.contact, name='contact'),
    path('student', views.student, name='student'),
    path('assessor', views.assessor, name='assessor'),
    path('students', views.students, name='students'),
    path('students/<int:id>', views.student_detail, name='student-detail'),
    path('sponsors', views.sponsors, name='sponsors'),
    path('assess/<int:id>', views.assess, name='assess'),
    path('fund/<int:id>', views.fund, name='fund'),
    path('search', views.search, name='search'),
    path('sponsor/<int:id>', views.sponsor_detail, name='sponsor-detail'),
    path('logout_sponsor', views.sponsor_logout, name='sponsor-logout'),
    path('logout_student', views.student_logout, name='student-logout'),
    path('logout_assessor', views.assessor_logout, name='assessor-logout'),
    path('donations', views.donations, name='donations'),
        
    ]