from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'bio', 'profile_picture']
        extra_kwargs = {
            'password': {'write_only': True}
        }

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.SerializersMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'token']
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        token, created = Token.objects.get_or_create(user=user)
        return user
    
    def get_token(self, obj):
        token = Token.objects.get(user=obj)
        return token.key
    
class LoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(username=data['username'], password=data['password'])
        if user and user.is_active:
            return {
                'user': user,
                'token': Token.objects.get_or_create(user=user)[0].key
            }
        raise serializers.ValidationError('Invalid credentials')
