from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from book.models import Book
from .models import Cart

def view_cart(request):
    return render(request, 'cart/view_cart.html')

@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, book=book)
    if not created:
        cart_item.quantity += int(request.POST['quantity'])
        cart_item.save()
    return redirect('view_cart')