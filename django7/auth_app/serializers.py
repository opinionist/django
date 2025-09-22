from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ("email", "name", "password", "role")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create_user(password = password, **validated_data)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Mata:
        model = CustomUser
        fields = ['id', 'email','name', 'role']
