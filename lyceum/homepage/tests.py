from django.test import TestCase, Client


# Create your tests here.
class StaticURLTests(TestCase):
    def test_homepage_endpoint(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_coffee_endpoint(self):
        response = Client().get('/coffee/')
        self.assertEqual(response.status_code, 418)
