from django import forms
from django.contrib.auth.models import User
from main_web_portal.models import UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta():
        model = User
        fields = ('username','email','password')
        help_texts = {
            'username': None,
            'email': None,
        }
        labels = {
            'username': 'Username',
            'email':'Email',
        }
        widgets = {
            'username': forms.TextInput({'placeholder': 'User name'}),
            'email': forms.TextInput({'placeholder': 'example@domain.com'}),
        }



class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('profile_pic','verification_code_lvl_1','address','url','verification_code_lvl_2',)
        widgets = {
            'verification_code_lvl_1': forms.TextInput({'placeholder': 'Enter Email Verification Code'}),
            'url': forms.TextInput({'placeholder': 'Enter URL of organization'}),
            'address': forms.TextInput({'placeholder': 'Enter Address'}),
            'verification_code_lvl_2': forms.TextInput({'placeholder': 'Enter Verification Token'})
        }

class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    class Meta():
        fields = ('username','password',)
        widgets = {
            'username': forms.TextInput({'placeholder': 'User name'}),
        }
