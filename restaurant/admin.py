from django.contrib import admin
from .models import Booking, MenuItem

admin.site.register(Booking)  # Register the Booking model
admin.site.register(MenuItem)  # Register the MenuItem model