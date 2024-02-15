from django.test import TestCase, Client


# Create your tests here.
class StaticURLTests(TestCase):
    def test_about_endpoint(self):
        response = Client().get('/about/')
        self.assertEqual(response.status_code, 200)
