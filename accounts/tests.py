from django.conf import settings
from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import logout, login, register, user_profile
from django.contrib.auth.models import User
from .models import UserProfile

# Create your tests here.

class TestAccountsUrls(TestCase):

    def test_logout_url_resolves_logout_view(self):
        path = resolve(reverse('account_logout'))
        self.assertEqual(path.func, logout)

    def test_login_url_resolves_login_view(self):
        path = resolve(reverse('account_login'))
        self.assertEqual(path.func, login)

    def test_register_url_resolves_register_view(self):
        path = resolve(reverse('register'))
        self.assertEqual(path.func, register)

    def test_user_profile_url_resolves_user_profile_view(self):
        path = resolve(reverse('user_profile', args=[1]))
        self.assertEqual(path.func, user_profile)

class TestAccountsModels(TestCase):

    def test_user_profile_model_returns_correct_str(self):
        self.test_user = User.objects.create(
            username='testUser',
            first_name='Test',
            last_name='User',
            email='test@test.com',
            password='Test12345!'
        )
        self.test_user.save()
        self.test_user_profile = UserProfile.objects.create(
            pk=1,
            phone_number = '01234567890',
            country = 'testCountry',
            county = 'testCounty',
            town_or_city = 'testTown',
            postcode = 'testPostcode',
            street1 = 'testStreet1',
            street2 = 'testStreet2',
            userID = self.test_user
        )
        self.test_user_profile.save()
        self.assertEqual(str(self.test_user_profile), '1  -  testUser')

class TestAccountsViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create_user('testUser', 'test@test.com', 'testPassword', first_name='Test', last_name='User')
        self.test_user.save()
        self.test_user_profile = UserProfile.objects.create(userID=self.test_user)

        self.logout_url = reverse('account_logout')
        self.login_url = reverse('account_login')
        self.register_url = reverse('register')
        self.user_profile_url = reverse('user_profile', args=[1])

    def test_logout_view_redirects_with_302_status_code_when_logged_in(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        
    def test_logout_view_redirects_to_index_when_logged_in(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.logout_url, follow=True)
        self.assertRedirects(response, reverse('index'))
        
    def test_login_GET_resolves_with_200_status_and_renders_login_html(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_POST_valid_form_and_is_authenticated_returned_to_index(self):
        response = self.client.post(self.login_url, {
            'username': 'testUser',
            'password': 'testPassword'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_login_POST_redirects_to_index_if_logged_in(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))

    def test_login_POST_throws_error_if_username_password_dont_match(self):
        response = self.client.post(self.login_url, {
            'username': 'testUser',
            'password': 'incorrectPassword'
        })
        self.assertEqual(str(list(response.context['messages'])[0]), 'Your username or password is incorrect')

    def test_register_GET_returns_status_code_200_and_renders_register_template(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_register_GET_redirects_to_index_if_logged_in(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.register_url)
        self.assertRedirects(response, reverse('index'), 302)

    def test_register_POST_creates_account_and_redirects_to_index(self):
        response = self.client.post(self.register_url, {
            'password1': 'testPassword',
            'password2': 'testPassword',
            'username': 'testUser2',
            'email': 'test2email@test.com',
            'first_name': 'Test2',
            'last_name': 'User2'
        })
        self.assertRedirects(response, reverse('index'), 302)
        self.assertEqual(User.objects.get(username='testUser2').email, 'test2email@test.com')

    def test_user_profile_GET_returns_status_200_and_renders_user_profile_page_when_logged_in(self):
        self.client.login(username='testUser', password='testPassword')
        response = self.client.get(self.user_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user-profile.html')

    def test_user_profile_GET_returns_status_302_if_not_logged_in(self):
        response = self.client.get(self.user_profile_url)
        self.assertEqual(response.status_code, 302)