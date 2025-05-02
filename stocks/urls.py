from django.urls import include, path
from . import views

app_name = 'stocks'
urlpatterns = [
    path('', views.stock_register, name = 'stock_register'), 
    path('stock_new', views.stock_new, name = "new-stock"),
    path('stock_query', views.stock_query, name="stock_query"),
    path('<slug:slug>', views.stock_page, name="page"),
    
]

