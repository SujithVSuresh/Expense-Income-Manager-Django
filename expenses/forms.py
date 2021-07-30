from django import forms
from django.forms import ModelForm, fields
from . models import Expense


class expenseForm(forms.ModelForm):

    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {'owner': forms.HiddenInput()}
    
