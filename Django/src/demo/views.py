from django.shortcuts import render
from django.http import HttpResponse
from .task import send_email


def index(request):
    send_email.delay('nandani@simformsolutions.com')
    return HttpResponse("Hi there!!!")
