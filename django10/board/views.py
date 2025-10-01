from rest_framework import generics, permissions
from .serializers import BoardSerializer
from .models import Board

class BoardGetView(generics.ListAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Board.objects.filter(writer = user)
    
class BoardSelectView(generics.ListAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        content = self.request.query_params.get("content")
        # content = self.kwargs.get("content")
        return Board.objects.filter(writer = user, content = content)
    
class BoardUpdateView(generics.UpdateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Board.objects.filter(writer = user)
    
class BoardDeleteView(generics.DestroyAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Board.objects.all()
    
class BoardCreateView(generics.CreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(writer = self.request.user)
