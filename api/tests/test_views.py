from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book 



class BookViewTest(APITestCase):
    
    def test_response_is_correct(self):
        book = Book.objects.create(
        title="Demo",
        description="Description",
        author="Author"
        )
        
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        returned_book = body[0]
        assert returned_book["title"]  == book.title
        assert returned_book["description"] == book.description
        assert returned_book["author"] ==  book.author