from django import forms
from . import models

class CreatePost(forms.ModelForm):
    
    class Meta:
        model = models.Stock
        fields = ("stock_id", "stock_name", "slug")
    