from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .forms import UserRegisterForm, AutoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class logout_view(LogoutView):
    next_page = '/'
def login_view(request):
    if request.user.is_authenticated:
        return redirect('main')
    if request.method == 'POST':
        form = AutoForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
    else:
        form = AutoForm()
    
    return render(request, 'users/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вы успешно зарегистрировались")
            return redirect('login')
        else:
            messages.error(request, "Ошибка регистрации")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
