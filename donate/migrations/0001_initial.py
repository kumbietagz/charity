# Generated by Django 3.2.3 on 2022-07-07 05:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('account_type', models.CharField(default='student', max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(max_length=50)),
                ('feesav', models.IntegerField()),
                ('dhav', models.IntegerField()),
                ('health', models.IntegerField()),
                ('residence', models.IntegerField()),
                ('fees', models.IntegerField()),
                ('fees_due', models.DateField()),
                ('school', models.CharField(max_length=200)),
                ('program', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=50)),
                ('approval', models.CharField(max_length=50)),
                ('confidence', models.FloatField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('account_type', models.CharField(default='sponsor', max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('dob', models.DateField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sponsor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funds', to='donate.sponsor')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='funds', to='donate.student')),
            ],
        ),
        migrations.CreateModel(
            name='Assessor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(default='assessor', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
