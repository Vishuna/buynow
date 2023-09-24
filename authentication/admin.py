from django.contrib import admin

from .models import *

# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display=('role_id','role_name',)



@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email')


@admin.register(CustomGroup)
class CustomGroupAdmin(admin.ModelAdmin):
    list_display=('g_id',)