from django import forms
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserInfo(User):
    age = models.IntegerField()
    contact = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)


class UserForm(UserCreationForm):
    class Meta:
        model = UserInfo
        fields = ['username', 'first_name', 'last_name', 'age',
                  'gender', 'contact', 'email', 'password1', 'password1']


class LoginForm(forms.Form):
    UserName = forms.CharField(max_length=30)
    Password = forms.CharField(max_length=30, widget=forms.PasswordInput)
