from django.contrib import admin
from .models import Booking, Menu

admin.site.register(Booking)  # Register the Booking model
admin.site.register(Menu)  # Register the MenuItem model