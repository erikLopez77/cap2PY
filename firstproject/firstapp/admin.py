from django.contrib import admin

# Register your models here.
from .models import Book
#para administrar el modelo en admin, lo registramos
admin.site.register(Book)