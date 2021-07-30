from django.urls import path
from . import views
import incomeSummary

app_name = 'incomeSummary'
urlpatterns = [
    path('', views.index, name="income-summary")
]