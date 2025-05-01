from django.shortcuts import render
from .models import Stock
from . import forms

# Create your views here.
def stock_register(request): 
    stocks = Stock.objects.all()
    return render(request, 'stocks/stock_register.html', {'stocks' : stocks})


def stock_page(request, slug): 
    try: 
            stock = Stock.objects.get(slug=slug)
    except: 
        return render(request, 'main.html')
    return render(request, 'stocks/stock_page.html', {'stock' : stock})

def stock_new(request):
    form = forms.CreatePost()
    return render(request, 'stocks/stock_new.html', {"form": form})
