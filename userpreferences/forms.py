from . models import *
from django import forms
from django.forms import ModelForm, fields

class PreferenceForm(forms.ModelForm):
    class Meta:
        model = UserPreference
        widgets = {'user': forms.HiddenInput()}
        fields = '__all__'
