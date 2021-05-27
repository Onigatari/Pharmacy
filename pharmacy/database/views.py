from django.shortcuts import render, redirect
from .models import Medicines, Category
from .forms import MedicinesForm

def database_home(request):
    medicines = Medicines.objects.order_by('count')
    category = Category.objects.all()

    return render(request, 'database/table.html', {'medicines': medicines, 'category': category})

def create(request):
    if request.method == 'POST':
        form = MedicinesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('database_home')

    form = MedicinesForm()
    
    data = {
        'form': form,
    }

    return render(request, 'database/create.html', data)