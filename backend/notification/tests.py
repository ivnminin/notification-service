from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_403_FORBIDDEN

from . import models
from . import serializers


class ClientTests(TestCase):

    number = 77777777
    code = 123
    tag = 'tag'
    gmt = 1

    def setUp(self):
        models.Client.objects.create(
            pk=1,
            number=self.number,
            code=self.code,
            tag=self.tag,
            gmt=self.gmt,
        )

    def test_model(self):
        client = models.Client.objects.get(pk=1)
        self.assertEqual(client.number, self.number)
        self.assertEqual(client.code, self.code)
        self.assertEqual(client.tag, self.tag)
        self.assertEqual(client.gmt, self.gmt)


class ClientTestsView(APITestCase):

    number = 77777777
    code = 123
    tag = 'tag'
    gmt = 1

    def setUp(self):
        self.client_ = models.Client.objects.create(
            pk=1,
            number=self.number,
            code=self.code,
            tag=self.tag,
            gmt=self.gmt,
        )

    def test_view(self):
        response = self.client.get('/api/clients/')
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_view_get_item(self):
        response = self.client.get('/api/clients/1/')
        serializer = serializers.ClientSerializer(self.client_)
        self.assertEqual(response.status_code, HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_view_get_does_not_exist_item(self):
        response = self.client.get('/api/clients/123/')
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_view_unsupported_method_post(self):
        response = self.client.post('/api/clients/1/', data={'mock': 123})
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_view_unsupported_method_put(self):
        response = self.client.put('/api/clients/1/', data={'mock': 123})
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_view_unsupported_method_patch(self):
        response = self.client.post('/api/clients/1/', data={'mock': 123})
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_view_unsupported_method_delete(self):
        response = self.client.delete('/api/clients/1/')
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
