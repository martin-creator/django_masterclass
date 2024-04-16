from django.urls import path, include
from rest_framework.routers import DefaultRouter

# from movielist_app.api.views import movie_list, movie_detail
from movielist_app.api.views import (WatchListCreateAPIView, WatchDetailAPIView, StreamPlatformListAPIView, StreamPlatformDetailAPIView, 
                                     ReviewListCreateAPIView, ReviewDetailAPIView, ReviewCreateAPIView, StreamPlatformVs)
# urlpatterns = [
#     path('list/', movie_list, name='movie_list'),
#     path('<int:pk>/', movie_detail, name='movie_detail'),
# ]

router = DefaultRouter()
router.register('stream', StreamPlatformVs, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListCreateAPIView.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAPIView.as_view(), name='movie_detail'),

    path('', include(router.urls)),
    # path('stream/', StreamPlatformListAPIView.as_view(), name='stream_list'),
    # path('stream/<int:pk>/', StreamPlatformDetailAPIView.as_view(), name='streamplatform-detail'),

    # path('review/,', ReviewListCreateAPIView.as_view(), name='review-list'),
    path('stream/<int:pk>/review/', ReviewCreateAPIView.as_view(), name='review-create'),
    path('stream/<int:pk>/review/', ReviewListCreateAPIView.as_view(), name='review-list'),
    path('stream/review/<int:pk>/', ReviewDetailAPIView.as_view(), name='review-detail')
]

# we use as_view() method to convert our class-based views into function-based views.