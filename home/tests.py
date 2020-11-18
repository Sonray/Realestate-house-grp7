from django.test import TestCase
<<<<<<< HEAD
from .models import *
=======
from .models import House
from django.contrib.auth import get_user_model
>>>>>>> 4c8ec86a9220764b7c20140ce80790886728b7e8

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
class HouseTestCase(TestCase):
    '''
    testcase class that runs tests for house objects
    '''

    def setUp(self):
        User=get_user_model()
        self.person = User(username = "daisy", email="daisy@email.com", password = "mypassword")
        self.person.save()
        self.home=House(
           description = 'Spacious bungalow',
           price = '12,000,000',
           category = 'bungalow',
           location = 'Kawangware',
           user=self.person
        )

    def test_instance(self):
        self.assertTrue(isinstance(self.home,House))

    def test_save_method(self):
        self.home.save_house()
        houses = House.objects.all()
        self.assertTrue(len(houses)>0)

    def test_update_method(self):
        self.home.save_house()
        self.home = House.objects.filter(description = 'Spacious bungalow').update(description = 'Nicely furnished')
        self.home_update = House.objects.get(category="bungalow")
        self.assertTrue(self.home_update.description== 'Nicely furnished')

    def test_delete_method(self):
        self.home.save_house()
        self.home=House.objects.get(user=self.person)
        self.home.delete_house()
        houses=House.objects.all()
        self.assertTrue(len(houses)==0)
