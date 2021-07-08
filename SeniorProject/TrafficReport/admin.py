from django.contrib import admin
from .models import TrafficPolice,Report,SystemAdmin,Notification,MobileNotification,MobileDevices
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
# Register your models here.

class UserCreationFormExtended(UserCreationForm):
  def __init__(self,*args,**kwargs):
    super(UserCreationFormExtended, self).__init__(*args,**kwargs)
    self.fields['is_staff']=forms.BooleanField(label=_("Traffic Police"),required=False)



class UserAdmin(BaseUserAdmin):
    ordering=['username']
    list_display=['username','first_name','email']
    add_form=UserCreationFormExtended

    fieldsets=(
        (None,{'fields':('username','password')}),
        (_('Personal Info'),{'fields':('first_name',)}),
        (
            _('Permissions'),
            ({'fields':('is_staff','is_active','is_superuser')})
        ),
        (_('Important dates'),{'fields':('last_login',)})
    )
    add_fieldsets=(
        (None, {
            'classes':('wide',),
            'fields':('username','password1','password2','is_staff')
        }),
    )




class ReportAdmin(admin.ModelAdmin):    
      list_per_page = 5
      list_display = ['description','records','traffic_police','status','created_at']
      def has_add_permission(self,request):
          return False



      def get_readonly_fields(self, request, obj=None):     
        return super(ReportAdmin, self).get_readonly_fields(
            request, obj=obj
        )

    

    


        

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(TrafficPolice)
admin.site.register(Report,ReportAdmin)
admin.site.register(SystemAdmin)
admin.site.register(Notification)
admin.site.register(MobileNotification)
admin.site.register(MobileDevices)