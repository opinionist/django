from django.contrib.auth import get_user_model
from .models import Comment
from rest_framework import serializers

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    writer = serializers.SlugRelatedField(
        read_only = True,
        slug_field = "email"
    )
    
    class Meta:
        model = Comment
        fields = '__all__'