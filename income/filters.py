from expenses.models import Category
from django_filters.filters import CharFilter, DateFilter, ModelChoiceFilter, NumberFilter
from . models import *
import django_filters
from django.forms.widgets import TextInput

class incomeFilter(django_filters.FilterSet):
    description = CharFilter(field_name='description', lookup_expr='icontains', label='Search description:', widget=TextInput(attrs={'placeholder': 'Search here'}))
    source = ModelChoiceFilter(queryset=Source.objects.all(), label='Search source')
    from_amount = NumberFilter(field_name='amount', lookup_expr='gte', label='Greater than or equal to:', widget=TextInput(attrs={'placeholder': 'Enter amount'}))
    to_amount = NumberFilter(field_name='amount', lookup_expr='lte', label='Less than or equal to:', widget=TextInput(attrs={'placeholder': 'Enter amoutn'}))
    from_date = DateFilter(field_name='date', lookup_expr='gte', label='On or after:', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    to_date = DateFilter(field_name='date', lookup_expr='lte', label='On or before:', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        Model = Income
        fields = '__all__'