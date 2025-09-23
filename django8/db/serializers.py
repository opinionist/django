from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer(write_only = True)
    # borrower = BorrowerSerializer(read_only=True)
    
    author = serializers.PrimaryKeyRelatedField(queryset = Author.objects.all())
    borrower = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset = get_user_model().objects.all())
    class Meta:
        model = Book
        fields = ['name', 'created_at', 'author', 'borrower']