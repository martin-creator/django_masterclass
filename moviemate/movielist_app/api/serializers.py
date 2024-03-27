from rest_framework import serializers

#     title = models.CharField(max_length=100)
#     genre = models.CharField(max_length=100)
#     year = models.IntegerField()
#     director = models.CharField(max_length=100)
#     plot = models.TextField()
#     poster = models.URLField(max_length=300)
#     trailer = models.URLField(max_length=300)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

class MovieSerializer(serializers.ModelSerializer):
# class meta is a class within a class 
# It is used to define metadata for the serializer class.
# Meta class is used to define the fields that we want to include in our serializer.
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    genre = serializers.CharField(max_length=100)
    year = serializers.IntegerField()
    director = serializers.CharField(max_length=100)
    plot = serializers.TextField()
    poster = serializers.URLField(max_length=300)
    trailer = serializers.URLField(max_length=300)
    created_at = serializers.DateTimeField(auto_now_add=True)
    updated_at = serializers.DateTimeField(auto_now=True)
