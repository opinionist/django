from rest_framework import serializers
from .models import Board
from django.contrib.auth import get_user_model

User = get_user_model()

class BoardSerializer(serializers.ModelSerializer):
    writer = serializers.SlugRelatedField(
        slug_field = "email",
        read_only = True
    )
    class Meta:
        model = Board
        fields = '__all__'