from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import Comment
from .serializers import CommentSerializer

User = get_user_model()

class CommentCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)

class CommentGetView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    def get_object(self):
        pk = self.request.query_params.get("pk")
        return get_object_or_404(Comment, pk=pk)

class CommentsGetView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(writer = user)
    
class CommentUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(writer = user)
    
class CommentDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        user = self.request.user
        return Comment.objects.filter(writer = user)