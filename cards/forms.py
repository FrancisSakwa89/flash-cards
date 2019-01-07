from django import forms
from .models import Profile,Card


class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    exclude = ['user']


class NewcardForm(forms.ModelForm):
  class Meta:
    model = Card
    exclude = ['user']    