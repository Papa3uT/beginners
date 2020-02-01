from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404, redirect
from test1.forms import MessagesForm,AddUserForm
from test1.models import Messages,AddUser
# Create your views here.

def index(request):
    if request.method == 'POST':
        form1 = MessagesForm(data=request.POST)
        if form1.is_valid():
            form1.save()
            print("Ok")
            return redirect("test1:index")  
    if request.method == 'POST':
        form2 = AddUserForm(data=request.POST)
        if form2.is_valid():
            form2.save()
            print("Ok")
            return redirect("test1:index")       
    mesage = Messages.objects.filter(chat_id=2)
    form1 = MessagesForm()
    form2 = AddUserForm()
    context = {'form1': form1,'form2': form2,}
    return render(request,"index.html", locals())
    return render(request,"index.html",{context})

def index_base(request):
    return HttpResponse("Ok ",status=200)

def testget(request):
     q = Messages.objects.filter(id=41)
     return HttpResponse(q)
     