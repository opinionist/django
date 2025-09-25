from rest_framework.response import Response
from .serializers import AuthorSerializer
from .models import Author
from rest_framework import generics, permissions

# Create your views here.
class AuthorGetView(generics.RetrieveAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Author.objects.all()
    lookup_url_kwarg = "email"
    lookup_field = "email"
    # def get_object(self):
    #     queryset = self.get_queryset()
    #     name = self.kwargs.get("name")
    #     email = self.kwargs.get("email")
    #     return generics.get_object_or_404(queryset, name=name, email=email)
    
class AuthorsGetView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    
class AuthorCreateView(generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]

class AuthorUpdateView(generics.UpdateAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Author.objects.all()
    lookup_url_kwarg = "email"
    lookup_field = "email"
    
    # def get_object(self):
    #     queryset = self.get_queryset()
    #     name = self.kwargs.get("name")
    #     email = self.kwargs.get("email")
    #     return generics.get_object_or_404(queryset, name = name, email = email)
    
class AuthorDeleteView(generics.DestroyAPIView):
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Author.objects.all()
    lookup_url_kwarg = "email"
    lookup_field = "email"

    # def get_object(self):
    #     queryset = self.get_queryset()
    #     name = self.kwargs.get("name")
    #     email = self.kwargs.get("email")
    #     return generics.get_object_or_404(queryset, name=name, email=email)