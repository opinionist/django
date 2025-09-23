from rest_framework.response import Response
from django.contrib.auth import authenticate
from .serializers import SignInSerializer, SignUpSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions
from .models import CustomUser

# Create your views here.
class SignInView(generics.GenericAPIView):
    serializer_class = SignInSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request,email = email, password = password)
        
        if not user:
            return Response({"error","유저의 회원 정보가 존재하지 않습니다."}, status=400)
        
        refresh = RefreshToken.for_user(user)
        return Response({"access" : str(refresh.access_token), "refresh": str(refresh), "user": SignInSerializer(user).data}, status=200)
    
class SignUpView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]
            