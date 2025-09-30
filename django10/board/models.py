from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Board(models.Model):
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("작성자"), on_delete=models.CASCADE)
    content = models.CharField(_("내용"), max_length=50)
    
    def __str__(self) -> str:
        return f'{self.writer.email}의 게시글'