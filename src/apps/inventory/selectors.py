from django.contrib.auth.models import User

from .models import Device


def get_devices():
    devices = Device.objects.all()
    data = [
        {
            "id": device.id,
            "brand": device.brand,
            "processor": device.processor,
            "disk": device.disk,
            "memory": device.memory,
            "type_device": device.type_device,
        }
        for device in devices
    ]
    return data


def get_devices_by_user():
    users = User.objects.all().prefetch_related("userdevice_set")
    data = []
    for user in users:
        data.append(
            {
                "User": user.first_name,
                "Devices": [
                    {
                        "id": related.device.id,
                        "brand": related.device.brand,
                        "processor": related.device.processor,
                        "disk": related.device.disk,
                        "memory": related.device.memory,
                        "type_device": related.device.type_device,
                    }
                    for related in user.userdevice_set.all()
                ],
            }
        )
    return data
