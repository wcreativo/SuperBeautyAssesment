from django.urls import path

from .views import AssignedDevicesView, DeviceView

urlpatterns = [
    path("devices/", DeviceView.as_view(), name="devices"),
    path("devices/assigned/", AssignedDevicesView.as_view(), name="assigned-devices"),
]
