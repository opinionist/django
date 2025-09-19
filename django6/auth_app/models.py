from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUser(AbstractUser):
    name = models.CharField(_("이름"), max_length=50, null = False, blank = False)
    email = models.EmailField(_("이메일"), max_length=254, null = False, blank = False, unique = True)
    ROLE_CHOICES = (
        ('admin', '관리자'),
        ('student', '학생'),
    )
    
    role = models.CharField(_(""), max_length=50, choices=ROLE_CHOICES, default='student')