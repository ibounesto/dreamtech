from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name','email',]

class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username','first_name','last_name','email','photo_profile']