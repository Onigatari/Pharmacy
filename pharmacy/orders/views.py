from django.shortcuts import render, redirect
from .models import Orders
from .forms import OrdersForm, OrdersFilterForm
from datetime import date

def order_index(request):
    orders = Orders.objects.order_by('registration_date')
    filter = OrdersFilterForm(request.GET)
    # if filter.is_valid():
    #     if filter.cleaned_data['select']:
    #         orders = orders.objects.get(received__iexact=True)

    return render(request, 'orders/orders.html', {'orders': orders, 'data': date.today, 'filter': filter }) 