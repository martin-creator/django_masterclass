from django.urls import path, include
from movielist_app import views

urlpatterns = [
    path('list/', views.movie_list, name='movie_list'),
    path('<int:pk>/', views.movie_detail, name='movie_detail'),
]