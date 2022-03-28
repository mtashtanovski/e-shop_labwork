from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2', 'email',)
