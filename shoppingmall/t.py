# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class CategoryCategory(models.Model):
    name = models.CharField(unique=True, max_length=20)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ItemItems(models.Model):
    name = models.CharField(max_length=20)
    reg_date = models.DateTimeField()
    price = models.SmallIntegerField()
    display = models.BooleanField()
    stock = models.BooleanField()
    file_url = models.CharField(max_length=200)
    image_url = models.CharField(max_length=200)
    category_id = models.ForeignKey(CategoryCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'item_items'


class ProductOption(models.Model):
    name = models.CharField(max_length=30)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_option'


class ProductOptionDetail(models.Model):
    name = models.CharField(max_length=30)
    option = models.ForeignKey(ProductOption, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_option_detail'


class ProductProduct(models.Model):
    name = models.CharField(max_length=30)
    price = models.SmallIntegerField()
    stock = models.BooleanField()
    display = models.BooleanField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField()
    file_url = models.TextField()
    image_url = models.TextField()
    category = models.ForeignKey(CategoryCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_product'


class UserAddress(models.Model):
    address = models.CharField(max_length=50)
    member = models.ForeignKey('UserUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_address'


class UserUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    is_admin = models.BooleanField()
    user_id = models.CharField(unique=True, max_length=50)
    phone_number = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'user_user'


class UserUserGroups(models.Model):
    customuser = models.ForeignKey(UserUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_groups'
        unique_together = (('customuser', 'group'),)


class UserUserUserPermissions(models.Model):
    customuser = models.ForeignKey(UserUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_user_permissions'
        unique_together = (('customuser', 'permission'),)
