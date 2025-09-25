from django.urls import path
from .views import AuthorGetView, AuthorCreateView, AuthorUpdateView, AuthorDeleteView, AuthorsGetView

urlpatterns = [
    path("get/<str:email>", AuthorGetView.as_view()),
    path('gets/',AuthorsGetView.as_view()),
    path("update/<str:email>", AuthorUpdateView.as_view()),
    path("delete/<str:email>", AuthorDeleteView.as_view()),
    path("create/", AuthorCreateView.as_view()),
]
