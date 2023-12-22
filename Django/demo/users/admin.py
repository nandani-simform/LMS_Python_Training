from django.contrib import admin
from .models import MyNewModel, Song

admin.site.register(MyNewModel)
admin.site.register(Song)
