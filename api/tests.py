from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book
from datetime import date

class BookModelTest(TestCase):
    def test_create_book(self):
        book = Book.objects.create(
            title="Test Book",
            author="Test Author",
            isbn="1234567890123",
            published_date="2020-01-01"
        )
        self.assertEqual(book.title, "Test Book")
        self.assertEqual(str(book), "Test Book by Test Author")

class BookAPITest(APITestCase):
    def setUp(self):
        self.book_data = {
            "title": "API Test Book",
            "author": "API Test Author",
            "isbn": "9876543210987",
            "published_date": "2021-01-01"
        }
        self.book = Book.objects.create(**self.book_data)
        self.url = reverse('book-list')

    def test_get_books(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book(self):
        new_book = {
            "title": "New Book",
            "author": "New Author",
            "isbn": "1111111111111",
            "published_date": "2022-01-01"
        }
        response = self.client.post(self.url, new_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_invalid_published_date(self):
        invalid_book = {
            "title": "Invalid Book",
            "author": "Invalid Author",
            "isbn": "2222222222222",
            "published_date": "2050-01-01"  # Future date
        }
        response = self.client.post(self.url, invalid_book, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
