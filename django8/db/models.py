from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
# Create your models here.

class Author(models.Model):
    name = models.CharField(_("이름"), max_length=50)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(_("책"), max_length=50)
    created_at = models.DateTimeField(_("만들어진 날짜"), auto_now_add=True)
    author = models.ForeignKey("Author", verbose_name=_("저자"), on_delete=models.CASCADE)
    borrower = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("빌린 사람"), on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name