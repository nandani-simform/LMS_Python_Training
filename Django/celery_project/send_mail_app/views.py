from django.shortcuts import render
from .tasks import send_email
from django.http import HttpResponse


def send_mail_to_all(request):
    # send_mail.delay()
    send_email.delay('nandani@simformsolutions.com')

    return HttpResponse('Sent')