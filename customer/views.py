from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer
from .forms import CustomerForm

def customer_home(request):
    customers = Customer.objects.all()
    return render(request, 'customer/home.html', {'customers': customers})

def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_home')
    else:
        form = CustomerForm()
    return render(request, 'customer/add_customer.html', {'form': form})

def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_home')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'customer/edit_customer.html', {'form': form})
