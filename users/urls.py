from django.urls import include, path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.user_list, name = 'user_list'), 
    path('register', views.register_view, name="register"),
    # path('<slug:slug>', views.user_page, name="page"),
    path('login', views.login_view, name="login"),
]