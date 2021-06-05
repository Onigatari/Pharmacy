from django.shortcuts import render, redirect
from .models import Orders, StatusOrder
from database.models import Medicines, Category
from .forms import OrdersForm, OrdersFilterForm
from datetime import date
from django.contrib.auth.decorators import login_required

@login_required
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
        orders = Orders.objects.all()
        if filter.cleaned_data['status']:
            orders = orders.filter(received__exact=filter.cleaned_data['status'])
        if filter.cleaned_data['find_category']:
            orders = orders.filter(medicines__category__exact=filter.cleaned_data['find_category'])
        if filter.cleaned_data['find_medicines']:
            orders = orders.filter(medicines__exact=filter.cleaned_data['find_medicines'])

    return render(request, 'orders/orders.html', {'orders': orders, 'filter': filter }) 

@login_required
def add_order(request):
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            item = Medicines.objects.get(pk=request.POST['medicines'])
            item.count = item.count - 1
            item.popularity = item.popularity + 1
            item.save()
            form.save()
            return redirect('orders')

    form = OrdersForm()
    
    
    return render(request, 'orders/add_order.html', { 'form': form })

@login_required
def order_get(request, id):
    try:
        order = Orders.objects.get(id=id)
        stat = StatusOrder.objects.get(status="Доставлен")
        order.received = stat
        order.save()
        return redirect('orders')
    except Orders.DoesNotExist:
        return redirect('orders')

@login_required
def order_delete(request, id):
    try:
        order = Orders.objects.get(id=id)
        order.delete()
        return redirect('orders')
    except Orders.DoesNotExist:
        return redirect('orders')