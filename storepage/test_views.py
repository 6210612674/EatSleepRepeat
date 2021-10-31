from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from users.models import *
from homepage.models import *

class StorepageViewTestCase(TestCase):

    def setUp(self):
        food = Food.objects.create(F_name="AAA", price=10, description="AAA", category=1)

        userstore = User.objects.create(username="user2340", password="1234", email="user@example.com", is_store=True)

        usercustomer = User.objects.create(username="user2345", password="1234", email="user@example.com", is_customer=True)

        food.registered_store.add(userstore)

    def test_index_view_status_code(self):
        """check status code"""

        c = Client()
        response = c.get(reverse('homepage:index'))
        self.assertEqual (response.status_code, 200)

    def test_addfood_view_page(self):
        userstore1 = User.objects.create(username="userstore1", password="1234", email="user@example.com", is_store=True)

        c = Client()
        c.force_login(userstore1)
        response = c.get(reverse('storepage:addfood'))
        self.assertEqual (response.status_code, 302)

    def test_statistic_view_page(self):

        c = Client()
        response = c.get(reverse('storepage:statistic'))
        self.assertEqual (response.status_code, 302)

    def test_storeitem_view_page(self):
        userstore1 = User.objects.create(username="userstore1", password="1234", email="user@example.com", is_store=True)


        c = Client()
        response = c.get(reverse('storepage:storeitem', args=(userstore1.id,)))
        self.assertEqual (response.status_code, 200)