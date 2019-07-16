from django.contrib.auth.models import AbstractUser
from django.db import models

from user.managers import CustomUserManager


class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    # is_staff = None
    # is_superuser = None
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=30, unique=False)
    user_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)

    USERNAME_FIELD = 'user_id'
    objects = CustomUserManager()
    EMAIL_FIELD = "admin@admin.com"
    # USER_ID_FIELD = []
    REQUIRED_FIELDS = ['username'] # superuser

    class Meta:
        db_table = "user_users"

    def __str__(self):
        return f'User : {self.username} , {self.user_id}'
