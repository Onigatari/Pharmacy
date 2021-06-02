from typing import List
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from database.models import Medicines


def main_index(request):
    medicines = Medicines.objects.order_by('-popularity')
    if 'q' in request.GET:
        q = request.GET['q']
        find = Medicines.objects.filter(name__icontains=q)
    else:
        find = None
    return render(request, 'main/main.html', {'medicines': medicines, 'find': find})
