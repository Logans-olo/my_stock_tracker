from django.shortcuts import render, redirect
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


def stock_query(request): 
    #raise Exception("HELLOETHEHREHRHE")
    print("request recieved")
    form = forms.QueryForm(request.POST or None)
    stocks = Stock.objects.none()  # Empty queryset by default
    
    if request.method == 'POST' and form.is_valid():
        filter_kwargs = {
            k: v for k, v in form.cleaned_data.items() 
            if v not in [None, '']
        }
        stocks = Stock.objects.filter(**filter_kwargs)
    print("rendering")
    return render(request, 'stocks/stock_query.html', 
                  {'stocks': stocks , "form": form})
    

def stock_new(request):
    #raise Exception("")
    print("Hello there")
    if request.method == 'POST': 
        form = forms.CreatePost(request.POST)
        if form.is_valid(): 
            newstock = form.save(commit=False)
            newstock.save()
            return redirect('stocks:stock_register')
    else:
        form = forms.CreatePost()
    return render(request, 'stocks/stock_new.html', {"form": form})
