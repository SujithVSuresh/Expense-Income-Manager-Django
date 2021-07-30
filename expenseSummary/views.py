from expenses.models import Expense
from django.shortcuts import render
from datetime import datetime, timedelta, time
from django.db.models import Sum
from . filters import expenseTotalFilter
from userpreferences.models import UserPreference

# Create your views here.
def index(request):

    expenses = Expense.objects.filter(owner=request.user)
    total_expenses = expenses.aggregate(Sum('amount'))
    currency = UserPreference.objects.get(user=request.user)
    
    #today = datetime.now().today()
    #today_filter = expenses.filter(today.year).aggregate(Sum('amount'))
    #month_filter = expenses.filter(date__month=today.month).aggregate(Sum('amount'))
    #year_filter = expenses.filter(date__year=today.year).aggregate(Sum('amount'))

    how_many_days = 7
    amount_by_days = expenses.filter(date__gte=datetime.now()-timedelta(days=how_many_days)).aggregate(Sum('amount'))
    
    year_monthly = request.GET.get('year_monthly')
    month_monthly = request.GET.get('month_monthly')
    monthly_expenses = expenses.filter(date__year=year_monthly, date__month=month_monthly).aggregate(Sum('amount'))

    year_yearly = request.GET.get('year_yearly')
    yearly_expenses = expenses.filter(date__year=year_yearly).aggregate(Sum('amount'))

    year_daily = request.GET.get('year_daily')
    month_daily = request.GET.get('month_daily')
    daily_daily = request.GET.get('daily_daily')
    daily_expenses = expenses.filter(date__year=year_daily, date__month=month_daily, date__day=daily_daily).aggregate(Sum('amount'))

    sum_of_daily = Expense.objects.filter(owner=request.user).values('date').order_by('-date').annotate(sum=Sum('amount'))
    
    filter = expenseTotalFilter(request.GET, queryset=sum_of_daily)
    sum_of_daily = filter.qs

    context = {'amount':amount_by_days, 'total_expenses':total_expenses, 'monthly_expenses':monthly_expenses, 'yearly_expenses':yearly_expenses, 'daily_expenses':daily_expenses, 
    'sum_of_daily':sum_of_daily, 'filter':filter, 'currency':currency}
    return render(request, 'expenseSummary/index.html', context)
