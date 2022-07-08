from django.contrib import admin
from .models import *
from django.contrib.auth.models import Permission

# Register your models here.
admin.site.register(Student)
admin.site.register(Assessor)
admin.site.register(Sponsor)
admin.site.register(Fund)
admin.site.register(Permission)