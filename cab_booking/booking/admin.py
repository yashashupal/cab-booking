# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Cab, Ride

admin.site.register(Cab)
admin.site.register(Ride)
