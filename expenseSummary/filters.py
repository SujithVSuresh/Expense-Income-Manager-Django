from expenses.models import Expense
import django_filters
from django_filters import DateFilter
from django.forms.widgets import TextInput


class expenseTotalFilter(django_filters.FilterSet):
    from_date = DateFilter(field_name='date', lookup_expr='gte', label='On or after:', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    to_date = DateFilter(field_name='date', lookup_expr='lte', label='On or before:', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    class Meta:
        Model = Expense
        fields = '__all__'