from django.forms import ModelForm
from .models import NewUser
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms

class Log_in_form(AuthenticationForm):
    class Meta:
        model=NewUser
        fields = ['username', 'password']

        widget={
            'username':forms.TextInput(attrs={'class':'fields'}),
            'password':forms.PasswordInput(attrs={'class':'fields'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = NewUser
        fields = ['user_name', 'email', 'password1', 'password2']