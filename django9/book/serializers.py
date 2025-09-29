from django.contrib.auth import get_user_model
from .models import Book
from author.models import Author
from rest_framework import serializers
from author.serializers import AuthorSerializer

class BookSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset = Author.objects.all(),
        slug_field="email",
        write_only = True
    )
    author_detail = AuthorSerializer(source = 'author', read_only = True)
    class Meta:
        model = Book
        fields = ['id', "name", "created_at", 'author', 'author_detail']
