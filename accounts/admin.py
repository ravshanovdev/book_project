from django.contrib import admin
from .models import CustomUser, Employee

admin.site.register([CustomUser, Employee])


