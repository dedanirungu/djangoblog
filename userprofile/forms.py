from django import forms
from django.contrib.auth.models import User
from .models import Profile

from captcha.fields import CaptchaField

GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
)


class UserForm(forms.ModelForm):

    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'required': 'true'}),
            'last_name': forms.TextInput(attrs={'required': 'true'}),
            'email': forms.TextInput(attrs={'type': 'email', 'required': 'true'}),
            'username': forms.TextInput(attrs={'required': 'true', 'pattern': '[a-z0-9\s]+'}),
            'password': forms.TextInput(attrs={'type': 'password', 'required': 'true'})
        }
        help_texts = {
            'username': None,
        }


class ManageUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password')
        widgets = {
            'first_name': forms.TextInput(attrs={'required': 'true'}),
            'last_name': forms.TextInput(attrs={'required': 'true'}),
            'email': forms.TextInput(attrs={'type': 'email', 'required': 'true'}),
            'username': forms.TextInput(attrs={'required': 'true', 'pattern': '[a-zA-Z0-9\s]+'}),
            'password': forms.TextInput(attrs={'type': 'password', 'required': 'true'})
        }
        help_texts = {
            'username': None,
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('gender', 'date_of_birth', 'phone', 'country', 'inviter', 'address', 'town',
                  'location', 'id_passport', 'email_again', 'password_again', 'year', 'month', 'date')
        widgets = {
            'phone': forms.TextInput(attrs={'required': 'true'}),
            'id_passport': forms.TextInput(attrs={'type': 'number', 'required': 'true'}),
            'country': forms.Select(attrs={'required': 'true'}),
            'address': forms.Textarea(attrs={'required': 'true'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'datepicker', 'required': 'true', "autocomplete": "off"}),
            'gender': forms.RadioSelect(attrs={'class': 'gender', 'required': 'true'}),
            'email_again': forms.TextInput(attrs={'type': 'email', 'required': 'true'}),
            'password_again': forms.TextInput(attrs={'type': 'password', 'required': 'true'}),
            'year': forms.Select(attrs={'required': 'true'}),
            'month': forms.Select(attrs={'required': 'true'}),
            'date': forms.Select(attrs={'required': 'true'}),
        }
