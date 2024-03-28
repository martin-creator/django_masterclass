from django.urls import path, include
# from movielist_app.api.views import movie_list, movie_detail
from movielist_app.api.views import MovieListCreateAPIView, MovieDetailAPIView

# urlpatterns = [
#     path('list/', movie_list, name='movie_list'),
#     path('<int:pk>/', movie_detail, name='movie_detail'),
# ]

urlpatterns = [
    path('list/', MovieListCreateAPIView.as_view(), name='movie_list'),
    path('<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
]

# we use as_view() method to convert our class-based views into function-based views.