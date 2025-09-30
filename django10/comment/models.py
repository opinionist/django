from django.db import models
from board.models import Board
from django.conf import settings
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Comment(models.Model):
    board = models.ForeignKey(Board, verbose_name=_("댓글"), on_delete=models.CASCADE)
    content = models.CharField(_("내용"), max_length=50)
    writer = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("작성자"), on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f'{self.writer.email}의 댓글'