from django.contrib.gis import admin
from .models import Records

# Register your models here.



admin.site.register(Records,admin.OSMGeoAdmin)