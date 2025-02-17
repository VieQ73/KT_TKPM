from django.contrib import admin
from .models import Book, Category

# Đăng ký Category và Book vào admin
admin.site.register(Category)
admin.site.register(Book)
