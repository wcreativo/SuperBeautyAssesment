from rest_framework import serializers

from .models import TypeDevice


class DeviceSerializer(serializers.Serializer):
    reference = serializers.CharField(max_length=255)
    brand = serializers.CharField(max_length=255)
    processor = serializers.CharField(max_length=255)
    disk = serializers.CharField(max_length=255)
    memory = serializers.CharField(max_length=255)
    type_device = serializers.ChoiceField(choices=TypeDevice.choices)
