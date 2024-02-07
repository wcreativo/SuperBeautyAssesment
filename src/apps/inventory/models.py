from django.contrib.auth.models import User
from django.db import models

from apps.core.models import GenericFields


class TypeDevice(models.TextChoices):
    LAPTOP = "laptop", "Laptop"
    TABLET = "tablet", "Tablet"
    DESKTOP = "desktop", "Desktop"


class Device(GenericFields):
    reference = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    processor = models.CharField(max_length=255)
    disk = models.CharField(max_length=255)
    memory = models.CharField(max_length=255)
    type_device = models.CharField(max_length=50, choices=TypeDevice.choices)

    def __str__(self):
        return f"{self.reference}"


class UserDevice(GenericFields):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    assignment_date = models.DateTimeField(blank=True, null=True)
    delivery_date = models.DateTimeField(blank=True, null=True)
