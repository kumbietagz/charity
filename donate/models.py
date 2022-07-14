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
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    gender = models.IntegerField(blank=True, null=True)
    feesav = models.IntegerField(blank=True, null=True)
    dhav = models.IntegerField(blank=True, null=True)
    health = models.IntegerField(blank=True, null=True)
    residence = models.IntegerField(blank=True, null=True)
    fees = models.IntegerField(blank=True, null=True)
    fees_due = models.DateField(blank=True, null=True)
    school = models.CharField(blank=True, null=True, max_length=200)
    program = models.CharField(blank=True, null=True, max_length=100)
    about = models.CharField(blank=True, null=True, max_length=50)
    forest = models.CharField(max_length=50, null=True, blank=True)
    approval = models.CharField(max_length=50, default="Pending")
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
    email = models.EmailField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
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