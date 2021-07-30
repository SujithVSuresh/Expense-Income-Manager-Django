from django.urls import path
from . import views

app_name = 'income'
urlpatterns = [
    path('', views.index, name='income'),
    path('add-income/', views.add_income, name='add-income'),
    path('edit-income/<str:id>/', views.edit_income, name='edit-income'),
    path('delete-income/<str:id>/', views.delete_income, name='delete-income'),
    path('export-excel/', views.export_excel, name='export-excel'),
]