from django.urls import path, include
from movielist_app.api import movie_list, movie_detail

urlpatterns = [
    path('list/', movie_list, name='movie_list'),
    path('<int:pk>/', movie_detail, name='movie_detail'),
]