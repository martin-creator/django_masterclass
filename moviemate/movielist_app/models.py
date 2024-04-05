from django.db import models

# Create your models here.

class StreamPlatform(models.Model):
    name = models.CharField(max_length=300)
    about = models.TextField()
    website = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class WatchList(models.Model):
    title = models.CharField(max_length=300)
    storyline = models.TextField()
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist') # related_name is used to access the related objects from the related object
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# class Movie(models.Model):
#     title = models.CharField(max_length=300)
#     genre = models.CharField(max_length=300)
#     year = models.IntegerField()
#     director = models.CharField(max_length=300)
#     plot = models.TextField()
#     poster = models.URLField(max_length=3000)
#     trailer = models.URLField(max_length=3000)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.title
