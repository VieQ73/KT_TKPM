from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'description', 'categories', 'publisher', 'publication_year', 'cover_image']
