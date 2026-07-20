from django.shortcuts import render

def home(request):
    context = {
        "title": "Main"
    }
    return render(request, "my_shop/home.html", context)

def about(request):
    context = {
        "title": "About"
    }
    return render(request, "my_shop/about.html", context)

def contact(request):
    context = {
        "phone": "+998 99 999 99 99"
    }
    return render(request, "my_shop/contact.html", context)
