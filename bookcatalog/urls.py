
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/', include('api.urls')),  # Include the API URLs
    path('admin/', admin.site.urls),
]
