
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('expenses.urls')),
    path('income/', include('income.urls')),
    path('authentication/', include('authentication.urls')),
    path('preferences/', include('userpreferences.urls')),
    path('expense-summary/', include('expenseSummary.urls')),
    path('income-summary/', include('incomeSummary.urls')),
    path('admin/', admin.site.urls),
]
