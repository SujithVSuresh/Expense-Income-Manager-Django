from income.models import Income
from django.shortcuts import redirect, render
from . forms import incomeForm
from django.contrib import messages
from django.core.paginator import Paginator
from userpreferences.models import UserPreference
from . filters import incomeFilter
from django.http import HttpResponse
from datetime import datetime
import xlwt


# Create your views here.

def index(request):
    owner = request.user
    income = Income.objects.filter(owner=owner)
    income_by_date = income.order_by('-date')
    currency = UserPreference.objects.get(user=request.user)

    filter = incomeFilter(request.GET, queryset=income_by_date)
    income_by_date = filter.qs
    
    #paginator
    paginator = Paginator(income_by_date, 5)
    page_number= request.GET.get('page')
    income_by_date = Paginator.get_page(paginator, page_number)
    
    context = {'income_by_date':income_by_date, 'currency':currency, 'filter':filter}
    return render(request, 'income/index.html', context)

def add_income(request):
    owner = request.user
    form = incomeForm(initial={'owner':owner})

    if request.method == 'POST':
        form = incomeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Income added successfully..')
            return redirect('income:income')
    context = {'form':form}
    return render(request, 'income/add_income.html', context)   

def edit_income(request, id):
    income = Income.objects.get(id=id)
    owner = request.user
    form = incomeForm(instance=income)

    if request.method == 'POST':
        form = incomeForm(request.POST, instance=income)
        if form.is_valid():
            form.save()
            messages.success(request, 'Income saved successfully..')
            return redirect('income:income')
    context = {'form':form}
    return render(request, 'income/edit_income.html', context) 

def delete_income(request, id):
    income = Income.objects.get(id=id)
    if request.method == 'POST':
        income.delete()
        messages.success(request, 'Income deleted successfully..')
        return redirect('income:income')

    
    context = {'income':income}
    return render(request, 'income/delete_income.html', context) 

def export_excel(request):
    response=HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Income' + \
        str(datetime.now())+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Income')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Amount', 'Description', 'Source', 'Date']

    for col_num in range(len(columns)):
        ws.write(row_num,col_num,columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = Income.objects.filter(owner=request.user).values_list('amount','description','source','date')

    for row in rows:
        row_num+=1

        for col_num in range(len(row)):
            ws.write(row_num,col_num,str(row[col_num]), font_style)    
    wb.save(response)      

    return response           
