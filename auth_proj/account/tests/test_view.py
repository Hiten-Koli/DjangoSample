from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class RegisterViewTestCase(APITestCase):
    def test_register_view_success(self):
        url = reverse('register')   
        data = {
                'email' : 'test@abc.com',
                'name' : 'xyz',
                'tc': 'True',
                'password' : 'tstpass',
                'password2' : 'tstpass',
            }   
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('refresh', response.data['token'])
        self.assertIn('access', response.data['token'])