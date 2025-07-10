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


# Create your views here.

class BookView(APIView):
    def get(self, request, *args, **kwargs):
        all_books = Book.objects.all()
        serializer = BookSerializer(all_books, many=True)
        return Response(serializer.data)

# Use this in your urls.py
book_view = BookView.as_view()
