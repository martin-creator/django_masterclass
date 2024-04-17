from rest_framework.decorators import api_view
from user_app.api.serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def registration_view(request):

    if request.method == 'POST':

        serializer = RegisterSerializer(data=request.data)
        
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['response'] = 'Successfully registered a new user.'
            data['username'] = account.username
            data['email'] = account.email

            token = Token.objects.get(user=account).key
        else:
            data = serializer.errors

        return Response(data)