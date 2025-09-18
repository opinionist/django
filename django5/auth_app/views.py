from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

User = get_user_model()

@csrf_exempt
def register(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        role = data.get("role" , "student")
        
        if User.objects.filter(username = username).exists():
            return JsonResponse({"error": "이미 존재하는 사용자"}, status=400)
        
        user = User.objects.create_user(username=username, password=password, role=role)
        return JsonResponse({"message": "회원가입 성공"}, status=201)
    
@csrf_exempt
def login_view(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data.get("username")
        password = data.get("password")
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = JsonResponse({"message": "로그인 성공", "role" : user.role})
            response.set_cookie("sessionid", request.session.session_key)  
            return response
        else:
            return JsonResponse({"error": "잘못된 사용자 이름 또는 비밀번호"}, status=400)