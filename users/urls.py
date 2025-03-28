from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.user_list, name = 'user_list'), 
]