from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils import timezone

from users.models import CustomUser


class CreateUserForm(UserCreationForm):
    username = forms.CharField(label=('username'), required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ('username'),
            'required': 'True',
        }
    ))
    user_id = forms.CharField(label=('user_id'), required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': ('user_id'),
            'required': 'True',
        }
    ))

    email = forms.EmailField(
        label=('Email'),
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': ('Email address'),
                'required': 'True',
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = {"username", "user_id", "password1", "password2", "email"}

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.last_login = timezone.now()
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()
        return user
