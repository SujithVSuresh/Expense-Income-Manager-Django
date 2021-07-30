from django_filters.filters import DateFilter
import django_filters
from django.forms.widgets import TextInput
from income.models import Income

class incomeTotalFilter(django_filters.FilterSet):
    from_date = DateFilter(field_name='date', lookup_expr='gte', label='On or after:', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))
    to_date = DateFilter(field_name='date', lookup_expr='lte', label='On or before:', widget=TextInput(attrs={'placeholder': 'YYYY-MM-DD'}))

    class Meta:
        Model = Income
        fields = '__all__'