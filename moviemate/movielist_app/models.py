from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
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
    # platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist') # related_name is used to access the related objects from the related object
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist')
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.PositiveIntegerField(validators=[  MinValueValidator(1), MaxValueValidator(5)])
    active = models.BooleanField(default=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    description = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # The difference between auto_now and auto_now_add is that auto_now will update the field every time the model is saved, while auto_now_add will only set the field when the model is first created.

    def __str__(self):
        return str(self.rating) + " | " + self.created_at.strftime("%d-%m-%Y") 


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
