# Generated by Django 3.2.3 on 2022-07-20 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0005_student_forest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='account_type',
        ),
        migrations.AddField(
            model_name='student',
            name='crowdfund',
            field=models.CharField(default='Ongoing', max_length=50),
        ),
    ]