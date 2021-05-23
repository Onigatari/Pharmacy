from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

class login_view(LoginView):
    template_name = 'users/login.html'
    
class logout_view(LogoutView):
    next_page = '/'