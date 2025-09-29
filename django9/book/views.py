from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .serializers import BookSerializer
from .models import Book
from author.models import Author
# Create your views here.

class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Book.objects.all()
    
class BookUpdateView(generics.UpdateAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Book.objects.all()
    def get_object(self):
        queryset = self.get_queryset()
        name = self.kwargs.get("name")
        author_email = self.kwargs.get("email")
        
        author = get_object_or_404(Author, email = author_email)
        return get_object_or_404(queryset, name = name, author = author)
    
class BookGetView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Book.objects.all()
    def get_object(self):
        queryset = self.get_queryset()
        name = self.kwargs.get("name")
        author_email = self.kwargs.get("email")
        
        author = get_object_or_404(Author, email = author_email)
        return get_object_or_404(queryset, name = name, author = author)
    
class BooksGetView(generics.ListAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Book.objects.all()

class BookDeleteView(generics.DestroyAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Book.objects.all()
    
    def get_object(self):
        queryset = self.get_queryset()
        name = self.kwargs.get("name")
        author_email = self.kwargs.get("email")
        
        author = get_object_or_404(Author, email = author_email)
        return get_object_or_404(queryset, name = name, author = author)
    