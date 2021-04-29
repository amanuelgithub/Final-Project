from django.contrib import admin

from django.contrib.admin import UserAdmin
from .models import Account

admin.site.register(Account)

# Register your models here.
