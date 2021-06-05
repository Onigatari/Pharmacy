from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('main/', include('main.urls'), name='main_panel'),
    path('admin/', admin.site.urls, name='admin_panel'),
    path('database/', include('database.urls'), name='database_panel'),
    path('', include('users.urls'), name='users_panel'),
    path('client/', include('client.urls'), name='client_panel'),
    path('orders/', include('orders.urls'), name='orders_panel'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)