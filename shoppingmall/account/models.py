from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class AccountManager(BaseUserManager):
    def create_superuser(self, *args, **kwargs):
        return super().create_superuser(*args, **kwargs)


class Account(AbstractUser):
    phone_number = models.CharField('PHONE_NUMBER', max_length=20, null=True, default="")
    objects = AccountManager()

    def __str__(self):
        return self.username

# class Account(models.Model):
#     REQUIRED_FIELDS = []
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     phone_number = models.CharField('PHONE_NUMBER', max_length=20)
