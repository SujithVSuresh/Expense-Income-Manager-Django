from . models import *
import django_filters
from django_filters import CharFilter, ModelChoiceFilter, DateFilter, NumberFilter
from django.forms.widgets import TextInput


class expenseFilter(django_filters.FilterSet):
    description = CharFilter(field_name='description', lookup_expr='icontains', label='Search description:', widget=TextInput(attrs={'placeholder': 'Search here'}))
    category = ModelChoiceFilter(queryset=Category.objects.all(), label='Search category:')
    from_amount = NumberFilter(field_name='amount', lookup_expr='gte', label='Greater than or equal to:', widget=TextInput(attrs={'placeholder': 'Enter Amount'}))
    to_amount = NumberFilter(field_name='amount', lookup_expr='lte', label='Less than or equal to:', widget=TextInput(attrs={'placeholder': 'Enter Amount'}))
    from_date = DateFilter(field_name='date', lookup_expr='gte', label='On or after:', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    to_date = DateFilter(field_name='date', lookup_expr='lte', label='On or before:', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    class Meta:
        Model = Expense
        fields = '__all__'