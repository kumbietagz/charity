# Generated by Django 3.2.3 on 2022-07-14 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_alter_student_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='forest',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]