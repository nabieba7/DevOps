from django.urls import re_path
from .views import book_view, health_view

app_name = 'api'

urlpatterns = [
    
    
    re_path(r'^books/$', book_view, name='books'
    )
    # Add more URL patterns as needed
]
