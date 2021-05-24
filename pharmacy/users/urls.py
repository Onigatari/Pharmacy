from django.urls import path
from .views import logout_view
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', logout_view.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]