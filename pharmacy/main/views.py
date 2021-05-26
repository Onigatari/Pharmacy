from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from database.models import Medicines

def main_index(request):
    medicines = Medicines.objects.order_by('-id')
    return render(request, 'main/main.html', {'medicines': medicines}) 
