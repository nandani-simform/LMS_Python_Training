from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    people = [
        {'name': 'Aman', 'age':22},
        {'name': 'Akshat', 'age':23},
        {'name': 'Naman', 'age':12},
        {'name': 'Tapan', 'age':30},
        {'name': 'Pransh', 'age':17},
        {'name': 'Daksh', 'age':18},

    ]  
    return render(request, "home/home.html", context={'page':'Home page',"people": people})

def about(request):
    context = {'page':'About page'}
    return render(request, "home/about.html", context)

def contact(request):
    context = {'page': 'Contact page'}
    return render(request, "home/contact.html", context)

def success_page(request):
    return HttpResponse("<h1>Hey, its success page</h1>")