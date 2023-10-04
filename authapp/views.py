from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, "login.html")

def validation(request):
    return render(request, "validation.html")

def home(request):
    return render(request, "home.html")
