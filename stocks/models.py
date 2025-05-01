from django.db import models
from datetime import date
class Stock(models.Model): 
    stock_id = models.CharField(max_length=4)
    stock_name = models.TextField()
    stock_time = models.DateTimeField(default=date.today)
    slug = models.SlugField()
# Create your models here.
