
from datetime import datetime, timedelta

from django.http import HttpResponse

from expenses.models import *
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from . forms import expenseForm
from django.contrib import messages
from userpreferences.models import UserPreference
from django.db.models import Sum
from django.core.paginator import Paginator
from . filters import expenseFilter
import xlwt

# Create your views here.

@login_required(login_url='login')
def index(request):
    currency = UserPreference.objects.get(user=request.user)
    expenses = Expense.objects.filter(owner=request.user)
    expenses_by_date = expenses.order_by('-date')
    
    #filter 
    filter = expenseFilter(request.GET, queryset=expenses_by_date)
    expenses_by_date = filter.qs

    #paginator
    paginator = Paginator(expenses_by_date, 5)
    page_number= request.GET.get('page')
    expenses_by_date = Paginator.get_page(paginator, page_number)

    context={'expenses_by_date':expenses_by_date, 'currency':currency, 'filter':filter,}
    return render(request, 'expenses/index.html', context)

def add_expense(request):
    
    owner = request.user
    form = expenseForm(initial={'owner':owner})
    if request.method == 'POST':
        form = expenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Amount added successfully..')
            return redirect('expenses:expenses')


    context = {'form':form}
    return render(request, 'expenses/add_expense.html', context)   

def edit_expense(request, id):
    expense = Expense.objects.get(id=id)
    edit_form = expenseForm(instance=expense)
    if request.method == 'POST':
        edit_form = expenseForm(request.POST, instance=expense)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Expense saved successfully..')
            return redirect('expenses:expenses')

    
    context={'edit_form':edit_form}
    return render(request, 'expenses/edit_expense.html', context)   

def delete_expense(request, id):
    expense = Expense.objects.get(id=id)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, 'Expense deleted successfully..')
        return redirect('expenses:expenses')

    context={'expense':expense}
    return render(request, 'expenses/delete_expense.html', context)   

def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Expenses' + \
        str(datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Expenses')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Amount', 'Description', 'Category', 'Date']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Expense.objects.filter(owner=request.user).values_list('amount','description','category','date')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]), font_style)    
    wb.save(response)      

    return response
    
