from django.contrib import admin
from .models import User, Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'date')