from django.shortcuts import render, redirect
from .models import Medicines
from .forms import MedicinesForm

def database_home(request):
    medicines = Medicines.objects.all()
    return render(request, 'database/table.html', {'medicines': medicines})

def create(request):
    if request.method == 'POST':
        form_push = MedicinesForm(request.POST)
        if form_push.is_valid():
            form_push.save()
            return redirect('database_home')

    form = MedicinesForm()

    data = {
        'form': form
    }

    return render(request, 'database/create.html', data)