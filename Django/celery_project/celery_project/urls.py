
from django.contrib import admin
from django.urls import path
from send_mail_app.views import send_mail_to_all

urlpatterns = [
    path("sendmail/", send_mail_to_all, name='mail'),

    path("admin/", admin.site.urls),
]
