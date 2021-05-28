from django.shortcuts import render, redirect
from .models import Medicines, Category
from .forms import MedicinesForm, MedicinesFilterForm

def database_home(request):
    medicines = Medicines.objects.order_by('price')
    
    filter = MedicinesFilterForm(request.GET)
    
    if filter.is_valid():
        if filter.cleaned_data['select']:
            medicines = Medicines.objects.filter(category__exact=filter.cleaned_data['select'])
            

    return render(request, 'database/table.html', {'medicines': medicines, 'filter': filter})

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