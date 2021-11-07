from django.test import TestCase, Client
from django.urls import reverse
from users.models import *
from homepage.models import *
csrf_client = Client(enforce_csrf_checks=True)


class StorepageViewTestCase(TestCase):

    def setUp(self):
        food = Food.objects.create(
            F_name="AAA", price=10, description="AAA", category=1)
        userstore = User.objects.create(
            username="user2340", password="1234", email="user@example.com", is_store=True)
        usercustomer = User.objects.create(
            username="user2345", password="1234", email="user@example.com", is_customer=True)
        food.registered_store.add(userstore)
        food.save()

    def test_index_view_status_code(self):
        """check status code"""

        c = Client()
        response = c.get(reverse('homepage:index'))
        self.assertEqual(response.status_code, 200)

    def test_addfood_view_page(self):
        userstore1 = User.objects.create(
            username="userstore1", password="1234", email="user@example.com", is_store=True)

        c = Client()
        c.force_login(userstore1)
        response = c.get(reverse('storepage:addfood'))
        self.assertEqual(response.status_code, 302)

    def test_addfood_view_page_notlogin(self):
        c = Client()
        response = c.get(reverse('storepage:addfood'))
        self.assertEqual(response.status_code, 302)

    def test_statistic_view_page_without_auth(self):
        c = Client()
        response = c.get(reverse('storepage:statistic'))
        self.assertEqual(response.status_code, 302)

    def test_statistic_view_page_with_auth(self):
        userstore = User.objects.create(
            username="userstore1", password="1234", email="user@example.com", is_store=True)
        c = Client()
        c.force_login(userstore)
        response = c.get(reverse('storepage:statistic'))
        self.assertEqual(response.status_code, 200)

    def test_storeitem_view_page(self):
        userstore1 = User.objects.create(
            username="userstore1", password="1234", email="user@example.com", is_store=True)

        c = Client()
        response = c.get(reverse('storepage:storeitem', args=(userstore1.id,)))
        self.assertEqual(response.status_code, 200)

    def test_addfoodview_view_page(self):
        userstore = User.objects.create(
            username="userstore1", password="1234", email="user@example.com", is_store=True)

        c = Client()
        c.force_login(userstore)
        response = c.get(reverse('storepage:addfoodview'))
        self.assertEqual(response.status_code, 200)

    def test_addfoodview_view_page_notlogin(self):
        c = Client()
        response = c.get(reverse('storepage:addfoodview'))
        self.assertEqual(response.status_code, 302)

    def test_additemfood_with_auth(self):
        user = User.objects.create(
            username="userstore1", password="1234", email="user@example.com", is_store=True)

        c = Client()
        c.force_login(user)
        response = c.post(reverse('storepage:addfood'), {
                          'foodname': 'krapra', 'price': 50.0, 'type': 1, 'description': 'aaa'})

        self.assertEqual(response.status_code, 302)

