from rest_framework import serializers
from movielist_app.models import Movie

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
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'year', 'director', 'plot', 'poster', 'trailer', 'created_at', 'updated_at']
        # id = serializers.IntegerField(read_only=True)
        # title = serializers.CharField(max_length=100)
        # genre = serializers.CharField(max_length=100)
        # year = serializers.IntegerField()
        # director = serializers.CharField(max_length=100)
        # plot = serializers.CharField()
        # poster = serializers.URLField(max_length=300)
        # trailer = serializers.URLField(max_length=300)
        # created_at = serializers.DateTimeField()
        # updated_at = serializers.DateTimeField()

    
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title) # get the value of title from validated_data and if it is not present, then get the value of title from instance
        instance.genre = validated_data.get('genre', instance.genre)
        instance.year = validated_data.get('year', instance.year)
        instance.director = validated_data.get('director', instance.director)
        instance.plot = validated_data.get('plot', instance.plot)
        instance.poster = validated_data.get('poster', instance.poster)
        instance.trailer = validated_data.get('trailer', instance.trailer)
        instance.save()
        return instance

# class MovieSerializer(serializers.ModelSerializer):
# class meta is a class within a class 
# It is used to define metadata for the serializer class.
# Meta class is used to define the fields that we want to include in our serializer.
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(max_length=100)
    # genre = serializers.CharField(max_length=100)
    # year = serializers.IntegerField()
    # director = serializers.CharField(max_length=100)
    # plot = serializers.CharField()
    # poster = serializers.URLField(max_length=300)
    # trailer = serializers.URLField(max_length=300)
    # created_at = serializers.DateTimeField(auto_now_add=True)
    # updated_at = serializers.DateTimeField(auto_now=True)

