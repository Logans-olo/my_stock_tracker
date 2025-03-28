from django.db import models

# Create your models here.
class User(models.Model): 
    user_id = models.IntegerField()
    username = models.TextField()
    password = models.TextField()
    
    def __str__(self):
        return self.username