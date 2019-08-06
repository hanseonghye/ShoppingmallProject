from django.contrib import admin
from .models import CustomUser as User
class UserAdmin(admin.ModelAdmin):
    search_fields = ("user_id",)

admin.site.register(User,UserAdmin)
