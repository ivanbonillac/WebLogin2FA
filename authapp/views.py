from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            return redirect('home')
            login(request, user)
        # Redirect to a success page.
        else:
            messages.success(request, ("Error de Inicio de Sesion"))
            return redirect('login')
        # Return an 'invalid login' error message.
    else:
        return render(request, "login.html", {})

def validation(request):
    return render(request, "validation.html")

def home(request):
    return render(request, "home.html")
