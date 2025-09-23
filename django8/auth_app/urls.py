from django.urls import path
from .views import SignInView, SignUpView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('sign_in/', SignInView.as_view()),
    path('sign_up/', SignUpView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
