from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Source(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Income(models.Model):
    amount = models.FloatField()
    date = models.DateField(default=now)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.source
