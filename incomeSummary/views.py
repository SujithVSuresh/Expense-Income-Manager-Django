from income.models import Income
from django.shortcuts import render
from .filters import incomeTotalFilter
from django.db.models import Sum
from . filters import incomeTotalFilter
from userpreferences.models import UserPreference

# Create your views here.

def index(request):

    currency = UserPreference.objects.get(user=request.user)
    
    sum_of_daily = Income.objects.filter(owner=request.user).values('date').order_by('-date').annotate(sum=Sum('amount'))
    filter = incomeTotalFilter(request.GET, queryset=sum_of_daily)
    sum_of_daily = filter.qs

    context = {'sum_of_daily':sum_of_daily, 'filter':filter, 'sum_of_daily':sum_of_daily, 'currency':currency}
    return render(request, 'incomeSummary/index.html', context)
