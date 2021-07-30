from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)  

    #to make categorys to categories in admin panel
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name      


class Expense(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="", null=True, blank=True)

    def __str__(self):
        return str(self.category)

