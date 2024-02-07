from .models import Device


def create_device(device_data):
    device = Device(**device_data)
    device.save()
    return device
