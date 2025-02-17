from django.urls import path
from . import views
from .views import edit_book

urlpatterns = [
    path('', views.list_books, name='list_books'),
    path('<int:book_id>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('books/<int:book_id>/edit/', edit_book, name='edit_book'), 
]
