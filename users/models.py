from django.db import models

# Create your models here.
class User(models.Model): 
    user_id = models.IntegerField()
    username = models.TextField()
    password = models.TextField()
    slug = models.SlugField()
    banner = models.ImageField(default='fallback.png', blank=True)
    def __str__(self):
        return self.username