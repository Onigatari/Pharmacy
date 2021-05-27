from django.shortcuts import render, redirect
from .models import Orders
from .forms import OrdersForm
from datetime import date

def order_index(request):
    orders = Orders.objects.order_by('registration_date')
    return render(request, 'orders/orders.html', {'orders': orders, 'data': date.today }) 
