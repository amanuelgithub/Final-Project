from django.contrib import admin
from .models import TrafficPolice,Report
# Register your models here.
class ReportAdmin(admin.ModelAdmin):    
      list_per_page = 5
      list_display = ['description','records','traffic_police','status','created_at']
      def get_readonly_fields(self, request, obj=None):     
        return super(ReportAdmin, self).get_readonly_fields(
            request, obj=obj
        )


admin.site.register(TrafficPolice)
admin.site.register(Report,ReportAdmin)