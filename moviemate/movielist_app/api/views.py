from rest_framework import status, generics, mixins, viewsets, serializers
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from movielist_app.models import WatchList, StreamPlatform, Review
from movielist_app.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from django.shortcuts import get_object_or_404
from movielist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly




class ReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self, serializer):
        # Get the watchlist id from the URL
        watchlist_pk = self.kwargs['pk']

        # Get the watchlist object
        watchlist = WatchList.objects.get(pk=watchlist_pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise serializers.ValidationError('You have already reviewed this movie')
        
        # Set the watchlist object to the review object
        serializer.save(watchlist=watchlist, review_user=review_user)


class ReviewListCreateAPIView(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ IsAuthenticatedOrReadOnly ]
    # permission_classes = [ AdminOrReadOnly ] # custom 

    # Override the get_queryset method to filter reviews by stream platform
    def get_queryset(self):
        # Get the stream platform id from the URL
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ ReviewUserOrReadOnly ] # custom permission

# class ReviewListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class ReviewDetailAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, pk):
#         return self.retrieve(request)
    
#     def put(self, request, pk):
#         return self.update(request)
    
#     def delete(self, request, pk):
#         return self.destroy(request)
    

class StreamPlatformVs(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


# class StreamPlatformVS(viewsets.ReadOnlyModelViewSet): # ReadOnlyModelViewSet is used to create a read-only view of the model
#     queryset = StreamPlatform.objects.all()
#     serializer_class = StreamPlatformSerializer
#    # It supports the following actions: list and retrieve
    

# class StreamPlatformVS(viewsets.ViewSet):

#     def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True, context={'request': request})
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = StreamPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=400)
    
#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         platform = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(platform, context={'request': request})
#         return Response(serializer.data)
    
    

class StreamPlatformListAPIView(APIView):
    def get(self, request):
        try:
            platforms = StreamPlatform.objects.all()
            serializer = StreamPlatformSerializer(platforms, many=True, context={'request': request})
            return Response(serializer.data)
        # capture any error and return a 400 status code
        except Exception as e:
            # print error to console
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
    

class StreamPlatformDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
            serializer = StreamPlatformSerializer(platform,context={'request': request})
            return Response(serializer.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class WatchListCreateAPIView(APIView):
    def get(self, request):
        try:
            movies = WatchList.objects.all()
            serializer = WatchListSerializer(movies, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=400)
    


class WatchDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    





# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
    
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request,pk):
    
#     if request.method == 'GET':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




