from rest_framework import serializers
from .models import Book

class BookSerializer(serializer.Serializer):
    class Mets:
        model = Book
        fields = ['title', 'description', 'author', 'created_at']