from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Service, Device, RepairOrder, ContactInfo


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'description')


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'user', 'created_at')
    list_filter = ('user',)
    search_fields = ('name', 'model', 'serial_number')


class RepairOrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'device', 'service', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'service')
    search_fields = ('device__name', 'device__model', 'user__username')


class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Device, DeviceAdmin)
admin.site.register(RepairOrder, RepairOrderAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)