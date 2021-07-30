from django.urls import path 
from . import views

app_name = 'expenseSummary'
urlpatterns = [
    path('', views.index, name="expense-summary")
]