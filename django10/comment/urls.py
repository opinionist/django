from django.urls import path
from .views import CommentCreateView,CommentGetView,CommentDeleteView,CommentUpdateView, CommentsGetView

urlpatterns = [
    path("create/", CommentCreateView.as_view()),
    path("get/", CommentGetView.as_view()),
    path("get/all/", CommentsGetView.as_view()),
    path("delete/<int:pk>/", CommentDeleteView.as_view()),
    path("update/<int:pk>/", CommentUpdateView.as_view()),
]
