from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


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
        return Response({
            "hello": "world",
        })

# Use this in your urls.py
book_view = BookView.as_view()
