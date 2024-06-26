from django.contrib import admin
from .models import Bus, Passenger, Pass

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_id', 'bus_name', 'bus_number')
    search_fields = ('bus_name', 'bus_number')

@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'age', 'email', 'contact')
    search_fields = ('name', 'email', 'contact')

@admin.register(Pass)
class PassAdmin(admin.ModelAdmin):
    list_display = ('passenger', 'bus')
    list_filter = ('bus', 'passenger__name')