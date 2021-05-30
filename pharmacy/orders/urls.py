from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_index, name='orders'),
    path('add_order', views.add_order, name='add_order'),
    path('delete/<int:id>/', views.order_delete),
    path('get/<int:id>/', views.order_get),
]