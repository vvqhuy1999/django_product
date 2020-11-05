from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import *
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username','email','phone']
    fieldsets = (*UserAdmin.fieldsets,
                    ('Thông tin khác',{
                        'fields': ['phone','name']
                    })
                )
admin.site.register(CustomUser,CustomUserAdmin)