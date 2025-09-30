from django.urls import path
from .views import BoardRegisterView, BoardLoginView
from rest_framework_simplejwt.views import TokenRefreshView
urlpatterns = [
    path("register/", BoardRegisterView.as_view()),
    path("login/", BoardLoginView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
