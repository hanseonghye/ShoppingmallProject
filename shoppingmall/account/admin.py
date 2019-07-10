from django.contrib import admin

from account.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('username',)


admin.site.register(Account, AccountAdmin)
