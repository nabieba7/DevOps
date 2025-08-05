from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book  # Assuming you have a Book model defined in models.py
from .serializers import BookSerializer  # Assuming you have a BookSerializer defined in serializers.py


class HealthView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "status": "ok",
        })

# Use this in your urls.py
health_view = HealthView.as_view()

class TestView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({
            "test": "ok",
        })
test_view = TestView.as_view()

# Create your views here.

class BookView(APIView):
    """  List all books , or creat a new book            """
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Use this in your urls.py
book_view = BookView.as_view()
