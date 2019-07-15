from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    first_name = None
    last_name = None
    # is_staff = None
    # is_superuser = None
    is_admin = models.BooleanField(default=False)

    user_id = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=50)

    objects = CustomUserManager()
    EMAIL_FIELD = "admin@admin.com"
    USER_ID_FIELD = []
    REQUIRED_FIELDS = ['user_id']

    def __str__(self):
        return f'{self.username} , {self.user_id}'
