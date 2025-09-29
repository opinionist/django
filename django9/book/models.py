from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings 
from author.models import Author
# Create your models here.

class Book(models.Model):
    name = models.CharField(_("책"), max_length=50)
    created_at = models.DateTimeField(_("출시일"), auto_now_add=True)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("빌린 사람"), on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(Author, verbose_name=_("작가"), on_delete=models.SET_NULL, null=True)
    
    class Meta:
        unique_together = ('name', 'author')