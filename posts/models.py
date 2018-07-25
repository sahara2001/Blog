from django.db import models

# Create your models here.

# !!! after changing model, type "python manage.py makemigrations" and "python manage.py migrate" in console to create database table
class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
