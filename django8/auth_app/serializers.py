from rest_framework import serializers
from .models import CustomUser

class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)       
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'role', 'name']
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser.objects.create_user(password = password, **validated_data)
        return user

class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'id', 'role', 'name']