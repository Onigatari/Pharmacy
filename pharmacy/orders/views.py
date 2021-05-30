from django.shortcuts import render, redirect
from .models import Orders, StatusOrder
from .forms import OrdersForm, OrdersFilterForm
from datetime import date

def order_index(request):
    orders = Orders.objects.order_by('registration_date')

    active = StatusOrder.objects.get(status="Активен")
    delivered = StatusOrder.objects.get(status="Доставлен")
    expired = StatusOrder.objects.get(status="Просрочен")

    for u in orders:

        entry = Orders.objects.get(pk=u.id)

        if u.received == delivered:
            continue
        elif u.extradition_date < date.today():
            stat = expired
            entry.received = stat
        elif u.extradition_date > date.today():
            stat = active
            entry.received = stat
        
        entry.save()

    filter = OrdersFilterForm(request.GET)

    if filter.is_valid():
        if filter.cleaned_data['status']:
            orders = Orders.objects.filter(received__exact=filter.cleaned_data['status'])

    return render(request, 'orders/orders.html', {'orders': orders, 'filter': filter }) 

def add_order(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')

    form = OrdersForm()
    
    return render(request, 'orders/add_order.html', { 'form': form })

def order_get(request, id):
    try:
        order = Orders.objects.get(id=id)
        stat = StatusOrder.objects.get(status="Доставлен")
        order.received = stat
        order.save()
        return redirect('orders')
    except Orders.DoesNotExist:
        return redirect('orders')

def order_delete(request, id):
    try:
        order = Orders.objects.get(id=id)
        order.delete()
        return redirect('orders')
    except Orders.DoesNotExist:
        return redirect('orders')