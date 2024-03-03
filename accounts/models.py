from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    # 用在 python manage.py createsuperuser
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True."))

        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50)
    description = models.CharField(max_length=256, blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    # 指定使用CustomUserManager
    objects = CustomUserManager()
    # 將User驗證時使用的Field改為email
    USERNAME_FIELD = "email"
    # 在創建User帳號時需要提供的Fields
    REQUIRED_FIELDS = ["username"]

    class Meta:
        # Model在後台的顯示名稱
        verbose_name = "Account"
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.email
