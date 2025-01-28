from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def stocks(request):
    template = loader.get_template('stocks.html')
    return HttpResponse(template.render())

def stock_ticker(request): 
    template = loader.get_template('stock_ticker.html')
    return HttpResponse(template.render())

def main(request): 
    template = loader.get_template('main.html')
    return HttpResponse(template.render())