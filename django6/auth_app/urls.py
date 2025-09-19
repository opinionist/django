from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.login_view, name = 'login_view'),
    path('sign_up/', views.sign_up, name = 'sign_up'),
]
