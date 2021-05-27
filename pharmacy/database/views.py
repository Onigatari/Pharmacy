from django.shortcuts import render, redirect
from .models import Medicines, Category
from .forms import MedicinesForm, MedicinesFilterForm

def database_home(request):
    medicines = Medicines.objects.order_by('count')
    category = Category.objects.all()
    filter = MedicinesFilterForm(request.GET)
    if filter.is_valid():
        if filter.cleaned_data['min_price']:
            medicines = medicines.filter(price__gte=filter.cleaned_data['min_price'])
        if filter.cleaned_data['max_price']:
            medicines = medicines.filter(price__lte=filter.cleaned_data['max_price'])
            
    return render(request, 'database/table.html', {'medicines': medicines, 'category': category, 'filter': filter})

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