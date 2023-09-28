from django.shortcuts import render
from django.http import HttpResponse
from .tasks import send_email


def index(request):
    send_email.delay('nandani@simformsolutions.com')
    return HttpResponse("send email")
