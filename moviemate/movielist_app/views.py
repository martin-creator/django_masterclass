from django.shortcuts import render
from movielist_app.models import Movie
from django.http import JsonResponse


def movie_list(request):
    movies = Movie.objects.all() # get all movies from database in QuerySet. A queryset is a list of objects of a given model
    data = {"movies": list(movies.values())} # convert QuerySet to list of dictionaries
    return JsonResponse(data)

def movie_detail(request, pk):
    movie = Movie.objects.get(pk=pk) # get movie from database
    data = {"movie": {
        "title": movie.title,
        "genre": movie.genre,
        "year": movie.year,
        "director": movie.director,
        "plot": movie.plot,
        "poster": movie.poster,
        "trailer": movie.trailer
    }}
    return JsonResponse(data)
