from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import User, Store

# Create your tests here.


class UserViewTestCase(TestCase):

    def setUp(self):
        User.objects.create(username="user1", password=make_password(
            '1234'), email="user1@example.com")
        userstore = User.objects.create(username="user2", password=make_password(
            '1234'), email="user2@example.com", is_store=True)
        store = Store.objects.create(
            user = userstore, location = "xxx", store_name = "xxx", type_store  = "xxx", place = "xxx", location_url = "xxx")

    def test_login_view_with_authentication(self):
        c = Client()
        user = User.objects.get(username="user1")
        c.force_login(user)
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_without_authentication(self):
        c = Client()
        user = User.objects.get(username="user1")
        response = c.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_success(self):
        c = Client()
        user = User.objects.get(username="user1")
        response = c.post(reverse('users:login'), {
                          'username': 'user1', 'password': '1234'})
        self.assertEqual(response.status_code, 302)

    def test_login_unsuccess(self):
        c = Client()
        user = User.objects.get(username="user1")
        response = c.post(reverse('users:login'), {
                          'username': '', 'password': ''})
        self.assertEqual(response.status_code, 200)

    def test_logout_success(self):
        c = Client()
        user = User.objects.get(username="user1")
        c.force_login(user)
        response = c.post(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)

    def test_customer_view_without_auth(self):
        user = User.objects.get(username='user1')
        c = Client()
        response = c.get(reverse('users:customer'))
        self.assertEqual(response.status_code, 302)

    def test_customer_view_with_auth(self):
        user = User.objects.get(username='user1')
        c = Client()
        c.force_login(user)
        response = c.get(reverse('users:customer'))
        self.assertEqual(response.status_code, 200)

    def test_store_view_without_auth(self):
        user = User.objects.get(username='user1')
        c = Client()
        response = c.get(reverse('users:store'))
        self.assertEqual(response.status_code, 302)

    def test_store_view_with_auth(self):
        userstore = User.objects.get(username='user2')
        c = Client()
        c.force_login(userstore)
        response = c.get(reverse('users:store'), args=(userstore.id,))
        self.assertEqual(response.status_code, 200)

    def test_favourite_successful(self):
        user1 = User.objects.get(username='user1')
        userstore = User.objects.get(username="user2")
        store = Store.objects.first()
        c = Client()
        c.force_login(user1)
        response = c.get(reverse('users:favourite', args=("2")))
        self.assertEqual(store.favourite.count(), 1)
        
        
    def test_favourite_successful2(self):
        user1 = User.objects.get(username='user1')
        userstore = User.objects.get(username="user2")
        store = Store.objects.first()
        store
        c = Client()
        c.force_login(user1)
        response = c.get(reverse('users:favourite', args=("2")))
        self.assertEqual(store.favourite.count(), 1)
    

    def test_favourite_view(self):
        user = User.objects.get(username='user1')
        c = Client()
        c.force_login(user)
        response = c.get(reverse('users:favourite_view', args=(user.id,)))
        self.assertEqual(response.status_code, 200)

    def test_customer_profile_successful(self):
        user = User.objects.get(username='user1')
        c = Client()
        c.force_login(user)
        # form = UpdateCustomerForm(entry=entry)
        # form = UpdateCustomerForm(request.POST, entry=entry)
        # self.assertTrue(form.is_valid())
        # form.save()
        response = c.post(reverse('users:customer_profile'), {
            'first_name': 'kkk',
        })
        self.assertEqual(response.status_code, 200)

    def test_store_profile(self):
        userstore = User.objects.get(username="user2")
        store = Store.objects.first()

        c = Client()
        c.force_login(userstore)
        response = c.post(reverse('users:store_profile'), {
            'user': userstore ,'store_name': 'kkk',
        })
        self.assertEqual(response.status_code, 200)



