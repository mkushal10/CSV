from django.contrib import admin

# Register your models here.
from .models import Employee # import model

admin.site.register(Employee) # Register model