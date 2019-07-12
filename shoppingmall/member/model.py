from django.db import models


class member(models.Model):
    name = models.CharField(max_length=50)
    member_id = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    is_staff = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        db_table = 'member_member'