from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserPreference(models.Model):

    CURRENCY = (
        ('INR', 'INR'),
        ('USD', 'USD'),
        ('EUR', 'EUR'),
        ('JPY', 'JPY'),
        ('CAD', 'CAD'),
        ('GBP', 'GBP'),
    )
       
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    currency = models.CharField(max_length=300, null=True, blank=True, choices=CURRENCY)

    def __str__(self):
        return str(self.user) + '-' + self.currency