from django import forms
from django.contrib.auth.models import User
from .models import Profile


GENDER_CHOICES = (
    (0, 'male'),
    (1, 'female'),
)


class UserForm(forms.ModelForm):


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

        fields = ('gender', 'date_of_birth', 'phone', 'address', 'town', 'location', )
        
        widgets = {
            'phone': forms.TextInput(attrs={'required': 'true'}),
            'address': forms.Textarea(attrs={'required': 'true'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'datepicker', 'required': 'true', "autocomplete": "off"}),
            'gender': forms.RadioSelect(attrs={'class': 'gender', 'required': 'true'}),
        }
