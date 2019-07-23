from django.test import TestCase, Client
from django.urls import resolve, reverse
from .views import index

# Create your tests here.
class TestHomeUrls(TestCase):
    """
    Test the URL for the home app
    """

    def test_index_url_resolves_to_index_view(self):
        path = resolve(reverse('index'))
        self.assertEqual(path.func, index)


class TestHomeViews(TestCase):
    """
    Test the URL for the home app
    """

    def test_index_GET(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200) 
        self.assertTemplateUsed(response, 'index.html')
        