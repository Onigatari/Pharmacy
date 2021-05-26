from django.shortcuts import render

def order_index(request):
    return render(request, 'orders/orders.html') 
