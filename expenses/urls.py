from django.urls import path
from . import views

app_name = 'expenses'
urlpatterns = [
    path('', views.index, name="expenses"),
    path('add-expense/', views.add_expense, name="add-expenses"),
    path('edit-expense/<str:id>/', views.edit_expense, name="edit-expenses"),
    path('delete-expense/<str:id>/', views.delete_expense, name="delete-expenses"),
    path('export-excel', views.export_excel, name="export-excel")
]