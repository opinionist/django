from django.urls import path
from .views import BookCreateView, BookGetView, BrowwoerUpdateView, AuthorCreateView, AuthorGetView

urlpatterns = [
    path("book/<int:pk>/", BookGetView.as_view(), name="book-get"),
    path("book/create/", BookCreateView.as_view(), name = "book-create"),
    path("book/update/", BrowwoerUpdateView.as_view(), name="book-update"),
    path("author/create/", AuthorCreateView.as_view(), name="author-create"),
    path("authors/get/", AuthorGetView.as_view(), name="authors-get"),
]
