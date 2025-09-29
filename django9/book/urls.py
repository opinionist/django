from django.urls import path
from .views import BookCreateView, BookDeleteView, BookGetView, BookUpdateView, BooksGetView

urlpatterns = [
    path("get/<str:name>/<str:email>", BookGetView.as_view()),
    path("gets/", BooksGetView.as_view()),
    path("delete/<str:name>/<str:email>", BookDeleteView.as_view()),
    path("update/<str:name>/<str:email>", BookUpdateView.as_view()),
    path("create/", BookCreateView.as_view()),
]
