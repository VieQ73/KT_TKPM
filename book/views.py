from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category
from django.db.models import Q
from faker import Faker
from customer.models import Customer
import random
from .forms import BookForm

def list_books(request):
    query = request.GET.get('q', '')  
    books = Book.objects.all().order_by("title")
    customers = Customer.objects.all()  # Lấy danh sách khách hàng

    if query:
        books = books.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query) |
            Q(publisher__icontains=query)
        )

    return render(request, 'book/list_books.html', {
        'books': books,
        'query': query,
        'customers': customers  # Truyền danh sách khách hàng vào template
    })

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/book_detail.html', {'book': book})

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Lưu sách vào database
            # Thêm thông báo sau khi thêm thành công
            return redirect('list_books')  # Chuyển hướng về trang danh sách sách
    else:
        form = BookForm()

    return render(request, 'book/add_book.html', {'form': form})

def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_detail", book_id=book.id)
    else:
        form = BookForm(instance=book)
    
    return render(request, 'book/edit_book.html', {'form': form, 'book': book})
