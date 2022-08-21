from django.contrib.auth import get_user_model
from django.test import TestCase

class UsersManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email = 'thayllonryanNormal17@gmail.com', password = 'foo')
        self.assertEqual(user.email, 'thayllonryanNormal17@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="foo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_user(email = 'thayllonryan17@gmail.com', password = 'foo')
        self.assertEqual(admin_user.email, 'thayllonryan17@gmail.com')
        self.assertTrue(admin_user.is_active)
        self.assertFalse(admin_user.is_staff)
        self.assertFalse(admin_user.is_superuser)

        try:
            self.assertNotIsInstance(admin_user, username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_superuser(email = 'thayllonryan17@gmail.com', password = 'foo', is_superuser = False)