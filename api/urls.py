from rest_framework.routers import DefaultRouter
from .views import BookViewSet, health_view, test_view, book_view
from django.urls import path, include

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')  # This creates the 'book-list' and 'book-detail' patterns

urlpatterns = [
    path('health/', health_view),
    path('test/', test_view),
    path('books-api/', book_view),  # optional: using your custom BookView
    path('', include(router.urls)),  # 🔑 Make sure this line is present
]
