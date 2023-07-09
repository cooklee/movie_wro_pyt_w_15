from django import forms
from django.contrib.auth.models import User


class AddUserForm(forms.ModelForm):
    password1 = forms.CharField(widget= forms.PasswordInput, label='Hasło')
    password2 = forms.CharField(widget= forms.PasswordInput, label='re-Hasło')

    class Meta:
        model = User
        fields = ['username', ]


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)