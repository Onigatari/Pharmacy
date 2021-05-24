from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import fields

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label = 'Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label= 'Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label= 'Повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label= 'E-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),   
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),   
        }

class AutoForm(AuthenticationForm):
    username = forms.CharField(label = 'Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label = 'Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'password')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),   
        }