from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category
from django.db.models import Q
from faker import Faker
import random
from .forms import BookForm

def list_books(request):
    query = request.GET.get('q', '')  # Lấy giá trị từ thanh tìm kiếm
    books = Book.objects.all().order_by("title")  # Sắp xếp theo tên sách

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(publisher__icontains=query)
        )

    return render(request, 'book/list_books.html', {'books': books, 'query': query})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_detail.html', {'book': book})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()

    return render(request, 'book/add_book.html', {'form': form})