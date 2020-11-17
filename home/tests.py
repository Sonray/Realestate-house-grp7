from django.test import TestCase

# Create your tests here.


class  ReviewtTestClass(TestCase):
    # Set up method
    def setUp(self):
        self. review = Review(id=1,post=self.post,user=self.user)
        self.post = Post(id=1,title='Test',content='This is a test',user = self.user)

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self. review, Review))