from rest_framework.decorators import api_view
from user_app.api.serializers import RegisterSerializer


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            return serializer.data