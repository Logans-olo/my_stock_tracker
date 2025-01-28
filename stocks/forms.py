from django import forms

class TickerForm(forms.Form): 
    stock_ticker = forms.CharField(label = "Stock Ticker", max_length=4)