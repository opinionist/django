from django.contrib import admin
from board.models import Board
from comment.models import Comment
from boarduser.models import BoardCustomUser

# Register your models here.
admin.site.register(Board)
admin.site.register(Comment)
admin.site.register(BoardCustomUser)