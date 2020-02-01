from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Users(models.Model):
    chat_id = models.IntegerField(blank=True, null=True,default=None)
    def __str__(self):
        return str(self.chat_id)

class AddUser(models.Model):
    password = models.CharField(default="", max_length=20)
    username = models.CharField(default="", max_length=15, unique=True)
    email = models.CharField(default="", max_length=30, unique=True)
    first_name = models.CharField(default="", max_length=15)
    last_name = models.CharField(default="", max_length=10)

class Messages(models.Model):
    chat = models.ForeignKey(Users,on_delete=models.CASCADE,default=None)
    headline = models.CharField(blank=True, null=True,default="",max_length=50)
    message = models.CharField(blank=True, null=True,default="",max_length=255)
    date_created = models.DateTimeField(blank=True, null=True,auto_now=True)
    
    def __str__(self):
        return str(self.chat_id)
