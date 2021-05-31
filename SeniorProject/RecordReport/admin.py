from django.contrib.gis import admin
from .models import Records,Vehicle

# Register your models here.

class VehicleAdmin(admin.ModelAdmin):
    list_display=('vehicle_plate','vehicle_type','vehicle_owner')

    





admin.site.register(Records,admin.OSMGeoAdmin)
admin.site.register(Vehicle,VehicleAdmin)