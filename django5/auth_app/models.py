from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin' , '관리자'),
        ('student' , '학생'),
        ('teacher' , '선생님'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')