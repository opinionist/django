from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from .serializers import BookSerializer, AuthorSerializer, BorrowerSerializer
from rest_framework import generics, permissions
from .models import Book, Author
# Create your views here.
class BookCreateView(generics.CreateAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class BookGetView(generics.RetrieveAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Book.objects.all()
    
class BrowwoerUpdateView(generics.GenericAPIView):
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def patch(self, request, *args, **kwargs):
        book_id = request.data.get("id")
        if not book_id:
            return Response({"error" : "책 ID를 입력해주세요."}, status= 400)
        try:
            book = Book.objects.get(pk = book_id) 
        except Book.DoesNotExist:
            return Response({"error": "책이 없습니다."}, status= 404)
        
        # if book.borrower and book.borrower != request.user:
        #     return Response({"error": "이미 다른 사람이 빌린 책입니다."}, status=403)

        book.borrower = request.user
        book.save()
        serializer = self.get_serializer(book)
        return Response(serializer.data)
    
class AuthorCreateView(generics.CreateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    
class AuthorGetView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Author.objects.all()