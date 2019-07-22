from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username, user_id, password, email, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, password=password, email=email, user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, user_id, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser create err')

        return self.create_user(username=username, user_id=user_id, password=password, email="admin@admin.com",
                                **extra_fields)
