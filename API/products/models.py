from django.db import models
from django.utils import timezone 

class Product(models.Model):
    name=models.CharField(max_length=50)
    count=models.IntegerField(default=0)
    company_name=models.CharField(max_length=50)
    register_date=models.DateTimeField(default=timezone.now)
