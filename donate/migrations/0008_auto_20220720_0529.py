# Generated by Django 3.2.3 on 2022-07-20 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0007_auto_20220720_0528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='crowdfund',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='student',
            name='fees',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='health',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
