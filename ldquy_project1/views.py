from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # File home.html sẽ nằm trong templates
