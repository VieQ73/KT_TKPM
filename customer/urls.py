from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_home, name='customer_home'),
    path('add/', views.add_customer, name='add_customer'),
    path('edit/<int:customer_id>/', views.edit_customer, name='edit_customer'),
]
