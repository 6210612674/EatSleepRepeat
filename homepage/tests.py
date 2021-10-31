from django.test import TestCase, Client
from django.urls import reverse
from homepage.models import *


# Create your tests here.

class HomepageViewTestCase(TestCase):

    def test_Food(self):
        food = Food.objects.create(F_name="rice", price=20.00, description="aroi", category=1)
        self.assertEqual(food.__str__(), f"1 rice 20.0 aroi 1")

    def test_Oder(self):
        order = Order.objects.create(amount=20.00)
        self.assertEqual(order.__str__(), f"1  : 20.0")

    def test_googlemap_view(self):
        c = Client()
        response = c.get(reverse('homepage:googlemap'))
        self.assertEqual(response.status_code, 200)

    def test_layout_view(self):
        c = Client()
        response = c.get(reverse('homepage:layout'))
        self.assertEqual(response.status_code, 200)

