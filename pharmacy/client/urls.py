from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_view, name='client'),
    path('add/', views.add_client_view, name='add_client')
]