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
        fields = ('profile_pic',)
