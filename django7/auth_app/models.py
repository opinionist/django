from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("이메일을 입력해주세요.")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        
        if user.role == "admin":
            user.is_staff = True
            user.is_superuser = True
        elif user.role == "teacher":
            user.is_staff = True
        
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, password = None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", "admin")
        return self.create_user(email, password, **extra_fields)
    
    def get_by_natural_key(self, email):
        return self.get(**{self.model.USERNAME_FIELD: email})
        

class CustomUser(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(_("이름"), max_length=50)
    email = models.EmailField(_("이메일"), max_length=254, unique = True)
    ROLE_CHOICES = (
        ('admin', '관리자'),
        ('student', '학생'),
        ('teacher', '교시'),
    )
    
    role = models.CharField(_("권한"), max_length=50, choices = ROLE_CHOICES, default = 'student')
    
    
    
    # def has_perm(self, perm, obj = None):
    #     return self.is_superuser
    
    # def has_module_perms(self, app_label):
    #     return self.is_superuser
     
    # @property
    # def is_staff(self):
    #     return self.role == 'admin'
    
    # @property
    # def is_superuser(self):
    #     return self.role == 'admin'
    
    is_active = models.BooleanField(default=True)   # 반드시 필요
    is_staff = models.BooleanField(default=False)   # 관리자 여부
    is_superuser = models.BooleanField(default=False)
    
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "role"]
    
    def __str__(self):
        return self.email