from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.

class BoardCustomManager(BaseUserManager):
    def create_user(self, email, password = None, **extra_fields):
        if not email:
            return ValueError("이메일을 입력하세요.")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        
        if(user.role == "admin"):
            user.is_staff = True
            user.is_superuser = True
        elif(user.role == "staff"):
            user.is_staff = True
        user.save(using = self.db)
        return user
    
    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD : email})
    
    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault("role", "admin")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class BoardCustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("이름"), max_length=50)
    email = models.EmailField(_("이메일"), max_length=254, unique=True)
    ROLE_CHOICES = (
        ('admin','관리자'),
        ('staff', '스태프'),
        ('user', '사용자')
    )
    role = models.CharField(_("권한"), max_length=50, choices=ROLE_CHOICES, default='user')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    
    objects = BoardCustomManager()
    
    REQUIRED_FIELDS = ["name", 'role']
    USERNAME_FIELD = "email"
    
    def __str__(self) -> str:
        return self.email