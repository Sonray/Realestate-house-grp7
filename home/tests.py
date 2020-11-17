from django.test import TestCase

# Create your tests here.


class  ReviewtTestClass(TestCase):
    # Set up method
  
    def setUp(self):
        self.user = User(id=1, username='barl', password='1234')
        self.user.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.user, User))

    def test_save_user(self):
        self.user.save()

    def test_delete_user(self):
        self.user.delete()