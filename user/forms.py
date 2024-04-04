
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile


class CustomUserCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", 'first_name')


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']