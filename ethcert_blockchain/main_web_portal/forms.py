from django import forms
from django.contrib.auth.models import User
from main_web_portal.models import UserProfile,Transaction

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ('profile_pic',)


class TransactionForm(forms.ModelForm):
    class Meta():
        model = Transaction
        fields = ('transaction_amount',
        'receiver','validity','certificate')
