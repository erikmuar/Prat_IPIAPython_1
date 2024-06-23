from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class Test1(TestCase):
    def test_numero1(self):
        url="/"
        
        request = self.client.get(url)
        
        self.assertEqual(reques.status_code,200)
        