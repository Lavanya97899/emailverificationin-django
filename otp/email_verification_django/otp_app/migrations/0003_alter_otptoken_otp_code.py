# Generated by Django 4.0.2 on 2023-12-30 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otp_app', '0002_otptoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptoken',
            name='otp_code',
            field=models.CharField(default='d2449f', max_length=6, unique=True),
        ),
    ]
