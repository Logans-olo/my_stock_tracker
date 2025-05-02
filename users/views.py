from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

# Create your views here.
def user_list(request): 
    users = User.objects.all()
    return render(request, 'users/users_list.html', {'users' : users})

# def user_page(request, slug): 
#     try: 
#             user = User.objects.get(slug=slug)
#     except: 
#         return render(request, 'main.html')
#     return render(request, 'users/user_page.html', {'user' : user})

def register_view(request): 
    if (request.method == "POST"):
        print("Printing to the console")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("The form is valid")
            form.save()
            
            return redirect("users:user_list")
    form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form })

def login_view(request): 
    if request.method == "POST": 
        form = AuthenticationForm(data=request.POST)
        if form.is_valid(): 
            #LOGIN HERE
            
            return redirect('stocks:stock_register')
    else: 
        form = AuthenticationForm()
    return render(request, 'users/login.html', {"form": form })
