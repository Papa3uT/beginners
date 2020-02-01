from django import forms
from test1.models import Messages,AddUser

class MessagesForm(forms.ModelForm):
    class Meta:
        fields = ('chat','headline','message')
        model = Messages

class AddUserForm(forms.ModelForm):
    class Meta:
        fields = ('password','username','email','first_name','last_name')
        model = AddUser