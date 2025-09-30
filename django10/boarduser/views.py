from rest_framework import generics, permissions
from .serializers import BoardLoginSerializer, BoardRegisterSerializer
from django.contrib.auth import authenticate, get_user_model
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
User = get_user_model()
class BoardRegisterView(generics.CreateAPIView):
    serializer_class = BoardRegisterSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    
class BoardLoginView(generics.GenericAPIView):
    serializer_class = BoardLoginSerializer
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all()
    
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        user = authenticate(request, email=email, password=password)
        if not user:
            return Response({"error":"존재하지 않는 유저 정보입니다."}, status=400)
        refresh = RefreshToken.for_user(user)
        return Response({
            "access": str(refresh.access_token),
            "refresh": str(refresh),
            "user": BoardLoginSerializer(user).data,
            }, status=202)
