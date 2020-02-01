from django.test import TestCase
from test1.models import Messages, Users
# Create your tests here.
import random

def create():
    for i in range(1,100):
        Messages.objects.create(chat_id=1,message="X")

m = Messages.objects.filter(chat_id__lte=50)
print(m)

def hello():
    try:
        m = Messages.objects.get(chat_id=48)

        print(m.message)

        m.message = "There"
        m.save()
    except Exception as e:
        print(e)

u , created = Users.objects.get_or_create(chat_id=3)
if created is True:
    print("creabefiw")
print(u,created)


create()
hello()