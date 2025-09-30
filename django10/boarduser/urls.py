from django.urls import path
from .views import BoardRegisterView, BoardLoginView

urlpatterns = [
    path("register/", BoardRegisterView.as_view()),
    path("login/", BoardLoginView.as_view())
]
