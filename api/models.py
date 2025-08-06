from django.db import models
from django.core.validators import MinLengthValidator

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(
        max_length=13,
        validators=[MinLengthValidator(13)],
        unique=True
    )
    description = models.TextField()  
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author}"