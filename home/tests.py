from django.test import TestCase
from .models import *
class TestInquiry(TestCase):
    def setUp(self):
        self.user = User
        self.user.save()
    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))
    def test_location_user(self):
        self.user.save()
    def test_contant_user(self):
        self.user.delete()