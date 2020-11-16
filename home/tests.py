from django.test import TestCase

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
