from django.contrib import admin
from core.models import Doctor
# Register your models here.

@admin.register(Doctor)
class Admin(admin.ModelAdmin):
    list_display = ('d_name','d_id','d_email','d_hos')
