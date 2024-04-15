from django.urls import path, include
# from movielist_app.api.views import movie_list, movie_detail
from movielist_app.api.views import WatchListCreateAPIView, WatchDetailAPIView, StreamPlatformListAPIView, StreamPlatformDetailAPIView, ReviewListCreateAPIView
# urlpatterns = [
#     path('list/', movie_list, name='movie_list'),
#     path('<int:pk>/', movie_detail, name='movie_detail'),
# ]

urlpatterns = [
    path('list/', WatchListCreateAPIView.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAPIView.as_view(), name='movie_detail'),

    path('stream/', StreamPlatformListAPIView.as_view(), name='stream_list'),
    path('stream/<int:pk>/', StreamPlatformDetailAPIView.as_view(), name='streamplatform-detail'),

    path('review/,', ReviewListCreateAPIView.as_view(), name='review-list')
]

# we use as_view() method to convert our class-based views into function-based views.