from django.contrib import admin

from .models import Device, UserDevice


class DeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "reference", "brand", "type_device")
    list_filter = ("type_device",)
    search_fields = ("reference",)


class UserDeviceAdmin(admin.ModelAdmin):
    list_display = ("id", "device", "user", "assignment_date")
    list_filter = ("assignment_date", "user")

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "device":
            kwargs["queryset"] = Device.objects.filter(userdevice__isnull=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(UserDevice, UserDeviceAdmin)
admin.site.register(Device, DeviceAdmin)
