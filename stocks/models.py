from django.db import models
from datetime import date
from django.contrib.auth.models import User
class Stock(models.Model): 
    stock_id = models.CharField(max_length=4)
    stock_name = models.TextField()
    stock_time = models.DateTimeField(default=date.today)
    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)
# Create your models here.
