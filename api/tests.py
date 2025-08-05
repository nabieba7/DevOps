from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book

class BookApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Optionally, create some sample books for testing
        Book.objects.create(title='Test Book 1', author='Author 1')
        Book.objects.create(title='Test Book 2', author='Author 2')

    def test_health_view(self):
        response = self.client.get('/api/')  # Adjust path if needed
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"status": "ok"})

    def test_test_view(self):
        response = self.client.get('/api/test/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"test": "ok"})

    def test_get_books(self):
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # We created 2 books in setUp

    def test_post_book_valid(self):
        data = {"title": "New Book", "author": "New Author"}
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], "New Book")

    def test_post_book_invalid(self):
        data = {"title": ""}  # Missing required fields or invalid data
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
