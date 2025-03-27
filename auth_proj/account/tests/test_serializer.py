from account.models import MyUser
from account.serializers import UserRegistrationSerialier
from rest_framework.test import APITestCase

class UserSerializerTestCase(APITestCase):
    def test_user_serializer_valid_data(self):
        data = {
            'email' : 'test@abc.com',
            'name' : 'xyz',
            'tc': 'True',
            'password' : 'tstpass',
            'password2' : 'tstpass',
        }
        serializer = UserRegistrationSerialier(data = data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

    def test_user_serializer_password_mismatch(self):
        data = {
            'email' : 'test@abc.com',
            'name' : 'xyz',
            'tc': 'True',
            'password' : 'tstpass',
            'password2' : 'misststpass',
        }   
        serializer = UserRegistrationSerialier(data = data)
        self.assertFalse(serializer.is_valid())
        self.assertEqual(serializer.errors['non_field_errors'][0],"Password & Conf Password Doesnt match")