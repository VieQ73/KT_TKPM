from django.contrib import admin
from django.urls import path, include
from ldquy_project1 import views  # Import view trang chủ

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Trang chủ chung
    path('customer/', include('customer.urls')),  # Trang của khách hàng
    path('cart/', include('cart.urls')),
    path('book/', include('book.urls')),
]
