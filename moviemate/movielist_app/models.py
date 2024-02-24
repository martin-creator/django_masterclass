from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.CharField(max_length=100)
    plot = models.TextField()
    poster = models.URLField(max_length=300)
    trailer = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
