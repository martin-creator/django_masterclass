from rest_framework.decorators import api_view
from user_app.api.serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)