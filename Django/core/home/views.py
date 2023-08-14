from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    people = [
        {'name': 'Nandani', 'age':22},
        {'name': 'Devanshi', 'age':23},
        {'name': 'Divisha', 'age':12},
        {'name': 'Harshal', 'age':30},
        {'name': 'Gautam', 'age':17},
        {'name': 'Jaysoni', 'age':18},

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