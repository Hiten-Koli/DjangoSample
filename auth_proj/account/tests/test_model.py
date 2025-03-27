from django.test import TestCase
from account.models import MyUser

# Create your tests here.
class UserModelTest(TestCase):
    def test_create_user(self):
        email = 'test@abc.com'
        name = 'xyz'
        password = 'passxyz'
        tc = True
        user = MyUser.objects.create_user(email=email, name=name, password=password, tc=tc)

        self.assertEqual(user.email, email)
        self.assertEqual(user.name, name)
        self.assertTrue(user.check_password(password))
        self.assertEqual(user.tc, tc)
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_admin )
        self.assertFalse(user.is_staff)

class UserMethodTest(TestCase):
    def test_has_perm(self):
        user = MyUser(email='test@abc.com', name='xyz')
        self.assertFalse(user.has_perm('some_permission'))