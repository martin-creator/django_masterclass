from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email' 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         validated_data['username'],
    #         password=validated_data['password']
    #     )
    #     return user