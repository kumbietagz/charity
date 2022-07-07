from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name="student", on_delete=models.CASCADE)
    account_type = models.CharField(default='student', max_length=50)
    image = models.ImageField(null=True, blank=True, editable=True, upload_to="images/")
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=15)
    email = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    gender = models.CharField( max_length=50)
    feesav = models.IntegerField()
    dhav = models.IntegerField()
    health = models.IntegerField()
    residence = models.IntegerField()
    fees = models.IntegerField()
    fees_due = models.DateField()
    school = models.CharField(max_length=200)
    program = models.CharField(max_length=100)
    about = models.CharField(max_length=50)
    approval = models.CharField(max_length=50)
    confidence = models.FloatField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True )
    updated = models.DateTimeField(auto_now = True)


class Sponsor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user = models.OneToOneField(User, related_name="sponsor", on_delete=models.CASCADE)
    account_type = models.CharField(default='sponsor', max_length=50)
    image = models.ImageField(null=True, blank=True, editable=True, upload_to="images/")
    dob = models.DateField(blank=True, null=True)
    phone = models.CharField(blank=True, max_length=15)
    email = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add = True )
    updated = models.DateTimeField(auto_now = True)

class Fund(models.Model):
    amount = models.IntegerField()
    sponsor = models.ForeignKey(Sponsor, related_name="funds", on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name="funds", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add = True )
    updated = models.DateTimeField(auto_now = True)


class Assessor(models.Model):
    user = models.OneToOneField(User, related_name="user", on_delete=models.CASCADE)
    account_type = models.CharField(default='assessor', max_length=50)