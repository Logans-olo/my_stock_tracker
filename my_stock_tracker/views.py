from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def stocks(request):
    return render(request, 'stocks.html')

def stock_ticker(request): 
    return render(request, 'stock_ticker')

def main(request): 
    return render(request, 'main.html')