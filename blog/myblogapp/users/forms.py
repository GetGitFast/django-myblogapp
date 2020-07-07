from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """ This class is used to extend the Django default form to include more fields such as email etc"""
    email = forms.EmailField()  # (required=True) is default. We could set (required=False)

    class Meta:
        """ Fields that need to be shown on the form from User model (default fields are username, password1, and
            password2). Also save these fields in the User table. That is why model = User"""
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
