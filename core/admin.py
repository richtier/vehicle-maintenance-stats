import datetime

from django.contrib import admin

from core import models


@admin.register(models.Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    search_fields = ('name', 'registration',)
    list_display = ('name', 'registration', 'year_manufactured',)


@admin.register(models.Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ('vehicle', 'date',)
    list_filter = ('vehicle', )


@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ( 'date', 'vehicle', 'type_of_service', 'miles',)
    list_filter = (
        'vehicle',
        'type_of_service',
        'oil',
        'diesel_filter',
        'air_filter',
    )
