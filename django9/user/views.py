from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, permissions
from .serializers import LoginSerializer, RegisterSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        
        if not user:
            return Response({"error" : "존재하지 않는 회원 정보입니다."}, status=400)
        
        refresh = RefreshToken.for_user(User)
        return Response({
            "refresh": str(refresh),
            "access" : str(refresh.access_token),
            "user" : LoginSerializer.data
        })