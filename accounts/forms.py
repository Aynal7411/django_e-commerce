from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile, Address


class UserRegisterForm(UserCreationForm):
   email = forms.EmailField(required=True)


class Meta:
   model = User
   fields = ("username", "email", "password1", "password2")


class UserProfileForm(forms.ModelForm):
   class Meta:
     model = UserProfile
     fields = ("phone", "avatar")


class AddressForm(forms.ModelForm):
  class Meta:
    model = Address
    fields = ("full_name", "phone", "line1", "line2", "city", "district","upozilla","postal_code", "is_default")