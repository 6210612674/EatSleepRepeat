from django.test import TestCase, Client
from django.urls import reverse
from users.models import * 

# Create your tests here.

class AboutViewTestCase(TestCase):
    
    def setUp(self):
        User.objects.create(username="user1", password="1234", email="user1@example.com")


    def test_index_view_page(self):
        c = Client()
        response = c.get(reverse('about:index'))
        self.assertEqual(response.status_code, 200)