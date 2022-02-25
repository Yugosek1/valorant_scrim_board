from django.test import TestCase

from django.contrib.auth import get_user_model
from accounts.models import Profile

User = get_user_model()

class AccountsTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        self.email = "test@gmail.com"
        self.password = "testpassword"
        super().__init__(*args, **kwargs)

    def setUp(self):
        user_obj = User(email=self.email)
        user_obj.set_password(self.password)
        user_obj.save()

    def test_profile_saved(self):
        counter = Profile.objects.count()
        self.assertEqual(counter, 1)
        profile_obj = Profile.objects.first()
        self.assertEqual(profile_obj.user.email, profile_obj.username)