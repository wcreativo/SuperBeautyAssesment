import json

import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from apps.inventory.models import Device

pytestmark = pytest.mark.django_db


class TestDevicesEndpoints:

    endpoint = "/inventory/devices/"

    def test_get_devices(self, api_client=APIClient):

        baker.make(Device, _quantity=10)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200

    def test_create(self, api_client=APIClient):
        device = baker.prepare(Device)
        expected_json = {
            "reference": device.reference,
            "brand": device.brand,
            "processor": device.processor,
            "disk": device.disk,
            "memory": device.memory,
            "type_device": device.type_device,
        }

        response = api_client().post(self.endpoint, data=expected_json, format="json")

        assert response.status_code == 201
        assert json.loads(response.content) == expected_json
