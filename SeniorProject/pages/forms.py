from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import fields

class CustomUserCreationForm(UserCreationForm):

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm, self).__init__(*args,**kwargs)
        self.fields['is_staff']=forms.BooleanField(label=("Traffic Police"),required=False)
    class Meta:
        model=User
        fields=UserCreationForm.Meta.fields+('is_staff',)


    