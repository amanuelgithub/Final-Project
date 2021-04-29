from django.contrib.gis import admin
from .models import Records,Vehicle

# Register your models here.
admin.site.register(Records,admin.OSMGeoAdmin)
admin.site.register(Vehicle,admin.OSMGeoAdmin)