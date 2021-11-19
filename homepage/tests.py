from django.test import TestCase, Client
from django.urls import reverse
from homepage.models import *
from users.models import *



# Create your tests here.

class HomepageViewTestCase(TestCase):

    def setUp(self):
        userstore = User.objects.create(
            username="user2340", password="1234", email="user@example.com", is_store=True)
        usercustomer = User.objects.create(
            username="user2345", password="1234", email="user@example.com", is_customer=True)
        store = Store.objects.create(
            user = userstore, location = "xxx", store_name = "xxx", type_store  = "xxx", place = "xxx", location_url = "xxx", status = "xxx")



    def test_Food(self):
        food = Food.objects.create(F_name="rice", price=20.00, description="aroi", category=1)
        self.assertEqual(food.__str__(), f"1 rice 20.0 aroi 1")

    def test_Oder(self):
        order = Order.objects.create(amount=20.00)
        self.assertEqual(order.__str__(), f"1  : 20.0")

    def test_Comment(self):
        comment = Comment.objects.create(comment_name="kkk", comment_text="aroi", rating=3)
        self.assertEqual(comment.__str__(), f"users.User.None : kkk  aroi")

    def test_googlemap_view(self):
        c = Client()
        response = c.get(reverse('homepage:googlemap'))
        self.assertEqual(response.status_code, 200)

    def test_layout_view(self):
        c = Client()
        response = c.get(reverse('homepage:layout'))
        self.assertEqual(response.status_code, 200)

    def test_search_view(self):
        c = Client()
        response = c.get(reverse('homepage:search'), {
                'search': 'xxx'})
        self.assertEqual(response.status_code, 200)

    def test_search_place_view(self):
        c = Client()
        response = c.get(reverse('homepage:store_search_place'), {
                'search': 'xxx'})
        self.assertEqual(response.status_code, 200)