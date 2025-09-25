from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Author(models.Model):
    name = models.CharField(_("작가"), max_length=50)
    email = models.EmailField(_("이메일"), max_length=254, unique=True)
    
    def __str__(self) -> str:
        return self.id