from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings 
# Create your models here.

class Book(models.Model):
    name = models.CharField(_("책"), max_length=50)
    created_at = models.DateTimeField(_("출시일"), auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)