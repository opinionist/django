from django.urls import path
from .views import BoardCreateView,BoardDeleteView,BoardSelectView, BoardUpdateView,BoardGetView

urlpatterns = [
    path("create/", BoardCreateView.as_view()),
    path("delete/<int:pk>", BoardDeleteView.as_view()),
    path("get/all/", BoardGetView.as_view()),
    path("get/<str:content>", BoardSelectView.as_view()),
    path("update/<int:pk>", BoardUpdateView.as_view()),
]