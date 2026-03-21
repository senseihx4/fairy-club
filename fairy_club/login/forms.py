from django import forms
from .models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email',  'password',  ]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'child_name', 'child_age']


class Fairytype(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'court_type']

class MembershipTypeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['membership_type']

