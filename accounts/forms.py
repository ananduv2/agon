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