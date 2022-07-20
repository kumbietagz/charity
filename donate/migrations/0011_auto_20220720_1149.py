# Generated by Django 3.2.3 on 2022-07-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0010_student_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='account_type',
        ),
        migrations.AlterField(
            model_name='student',
            name='about',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
