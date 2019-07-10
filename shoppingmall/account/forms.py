from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import Account


class AccountSignForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ('username', 'email', 'phone_number')