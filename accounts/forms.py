from .models import *
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm

class AddEventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class StudentSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields =['username','password1','password2']

class DataForm(ModelForm):
    class Meta:
        model = Account
        fields = ['name','email']

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['url']

class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ['result']

class AddLivedEventForm(ModelForm):
    class Meta:
        model = LiveEvent
        fields = ['name','url','date','time','details']

class EditStudentProfile(ModelForm):
    class Meta:
        model = Account
        fields = ['name','email','profilepic','mob']

class EditAdminProfile(ModelForm):
    class Meta:
        model = Account
        fields = ['name','email','profilepic','mob']