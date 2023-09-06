from django.shortcuts import render, redirect

def Profile(request):
    return render(request, 'users/profile.html')
