from django.contrib.auth import authenticate, login, get_user_model
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from rest_framework import status
import json

User = get_user_model()

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "로그인 성공", "role" : user.role},status = 200,)
        else :
            return JsonResponse({"error" : "로그인 실패"}, status = 400)
        
@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        try:
            validate_email(email)
        except ValidationError :
            return JsonResponse({"error" : "이메일 형식이 이상합니다."}, status = 400)
        
        name = data.get('name')
        if not name :
            return JsonResponse({"error" : "이름이 존재하지 않습니다."}, status = 400)
        username = data.get('username')
        password = data.get('password')
        role = data.get('role', 'student')
        if role not in dict(User.ROLE_CHOICES):
            return JsonResponse({"error" : "존재하지 않는 권한입니다."}, status = 400)
        
        try:
            user = User.objects.create_user(username = username, password = password, role = role, email = email)
            if role == "admin":
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return JsonResponse({"message" : "유저를 생성했습니다"}, status = 200)
        except IntegrityError as e : 
            if 'username' in str(e):
                return JsonResponse({"error": "닉네임이 중복됩니다."}, status=400)
            elif 'email' in str(e):
                return JsonResponse({"error": "이메일이 중복됩니다."}, status=400)
            else:
                return JsonResponse({"error": "회원가입 실패"}, status=400)
