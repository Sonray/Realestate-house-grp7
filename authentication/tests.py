from django.test import TestCase
from rest_framework.test import APITestCase
from django.urls import reverse
from .models import User
# Create your tests here.
class Test_set_up(APITestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

        user_detail= {
            'username':'David',
            'email':'David@gmail.com',
            'password':'David',
        }


        return super().setUp()

    def tearDown(self):
        return super().tearDown()

class Test_auth_views(Test_set_up):

    def Test_register_with_no_data(self):
        res = self.client.post(self.register_url)
        self.assertEqual(res.status_code, 400)

    def Test_register_user_data(self):
        res = self.client.post(self.register_url, self.user_detail, format='json')
        self.assertEqual(res['username'], self.user_detail['username'])
        self.assertEqual(res['email'], self.user_detail['email'])
        self.assertEqual(res['password'], self.user_detail['password'])
        self.assertEqual(res.status_code, 201)

    def test_unverified_email(self):
        self.client.post(self.register_url, self.user_detail, format='json')
        res = self.client.post(self.login_url, self.user_detail, format='json')
        self.assertEqual(res.status_code, 401)

    def test_login(self):
        response = self.client.post(self.register_url, self.user_detail, format='json')
        email = response.data['email']
        user = User.objects.get(email=email)
        user.is_authenticated = True
        user.save()
        res = self.client.post(self.login_url, self.user_detail, format='json')
        self.assertEqual(res.status_code, 200)
