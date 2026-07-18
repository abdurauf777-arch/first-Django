from django.shortcuts import render

def home(request):
    return render(request, "my_shop/home.html")

def about(request):
    return render(request, "my_shop/about.html")

def contact(request):
    return render(request, "my_shop/contact.html")