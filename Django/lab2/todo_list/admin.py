from django.contrib import admin
from .models import ToDo  # can use * to import all models

# Register your models here.

admin.site.register(ToDo)
