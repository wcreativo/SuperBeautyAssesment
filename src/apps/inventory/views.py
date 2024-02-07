import logging

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .selectors import get_devices, get_devices_by_user
from .serializers import DeviceSerializer
from .services import create_device


class DeviceView(APIView):

    def get(self, request):
        devices = get_devices()
        return Response(devices, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            create_device(serializer.data)
            logger.info("Device created successfully: %s", serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error("Validation error occurred: %s", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssignedDevicesView(APIView):

    def get(self, request):
        assigned_devices = get_devices_by_user()
        return Response(assigned_devices, status=status.HTTP_200_OK)


logger = logging.getLogger(__name__)
