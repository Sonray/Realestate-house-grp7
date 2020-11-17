from django.test import TestCase
from .models import *

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(id=1, username='Michael', password='rujq@345')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()
# Create your tests here.

class ReviewTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.user= User(id=1,title='Test',content='This is a test',user = self.user)
        self.review = Review(id=1,post=self.post,user=self.user)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.review ,Review ))
