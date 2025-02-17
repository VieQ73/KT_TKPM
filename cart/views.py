from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Cart, CartItem
from book.models import Book
from customer.models import Customer
from decimal import Decimal

def add_to_cart(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        quantity = int(request.POST.get("quantity", 1))
        customer_id = request.POST.get("customer_id")

        book = get_object_or_404(Book, id=book_id)
        customer = get_object_or_404(Customer, id=customer_id)

        # Kiểm tra xem khách hàng đã có giỏ hàng chưa, nếu chưa thì tạo mới
        cart, created = Cart.objects.get_or_create(customer=customer)

        # Kiểm tra xem sách đã có trong giỏ chưa
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book, defaults={"quantity": quantity})
        if not created:
            cart_item.quantity += quantity
            cart_item.save()

        return JsonResponse({"success": True, "message": "Sách đã được thêm vào giỏ hàng!"})

    return JsonResponse({"success": False, "message": "Có lỗi xảy ra!"})


def view_cart(request):
    carts = Cart.objects.prefetch_related("items__book").all()
    cart_totals = []  # Danh sách để lưu tổng tiền của mỗi giỏ hàng

    for cart in carts:
        total_price = Decimal(0)  # Khởi tạo tổng tiền cho giỏ hàng này
        for item in cart.items.all():
            # Kiểm tra và chuyển đổi Decimal128 sang Decimal nếu cần
            price = Decimal(item.book.price.to_decimal()) if hasattr(item.book.price, 'to_decimal') else Decimal(item.book.price)
            total_price += price * item.quantity
        
        # Thêm tổng tiền của giỏ hàng vào danh sách
        cart_totals.append({"cart": cart, "total_price": total_price})

    # Trả về giỏ hàng và tổng tiền của từng giỏ
    return render(request, "cart/view_cart.html", {"cart_totals": cart_totals})
