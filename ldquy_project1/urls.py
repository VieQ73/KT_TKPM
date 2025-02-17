from django.contrib import admin
from django.urls import path, include
from ldquy_project1 import views  # Import view trang chủ
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Trang chủ chung
    path('customer/', include('customer.urls')),  # Trang của khách hàng
    path('cart/', include('cart.urls')),
    path('book/', include('book.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)