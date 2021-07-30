from django import forms
from django.db import models
from django.forms import ModelForm, fields
from . models import Income


class incomeForm(forms.ModelForm):

    class Meta:
        model = Income
        fields = '__all__'
        widgets = {'owner': forms.HiddenInput()}
        