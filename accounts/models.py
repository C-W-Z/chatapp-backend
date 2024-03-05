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
        UserProfile.objects.create(user=user)
        return user

    # 繞過驗證創建superuser
    # python manage.py shell
    # from django.contrib.auth import get_user_model
    # User = get_user_model()
    # User.objects.create_superuser('admin', 'admin')

    # 用在 python manage.py createsuperuser
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("username", "admin")

        if extra_fields.get("is_staff") is not True:
            raise ValueError(("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(("Superuser must have is_superuser=True."))

        return self.create_user(email=email, password=password, **extra_fields)

class User(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(max_length=50, blank=True)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    # 指定使用CustomUserManager
    objects = CustomUserManager()
    # 將User驗證時使用的Field改為email
    USERNAME_FIELD = "email"
    # 在createsuperuser時需要提供的Fields
    REQUIRED_FIELDS = ["username"]

    class Meta:
        # Model在後台的顯示名稱
        verbose_name = "Account"
        verbose_name_plural = 'Accounts'

    def __str__(self):
        return self.email

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        # Model在後台的顯示名稱
        verbose_name = "User Profile"
        verbose_name_plural = 'User Profiles'

    def __str__(self):
        return self.user.email
