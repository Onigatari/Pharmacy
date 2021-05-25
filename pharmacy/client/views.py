from django.shortcuts import render
from .models import Client

def client_view(request):
    client = Client.objects.order_by('name')
    return render(request, 'client/client.html', {'client': client})

def add_client_view(request):
    return render(request, 'client/add_client.html')