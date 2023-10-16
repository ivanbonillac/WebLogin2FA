from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import send_otp
from datetime import datetime
import pyotp
from django.contrib.auth.models import User


# Create your views here.
def login_view(request):
    error_message = None
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            #OTP Feature
            send_otp(request)
            request.session["username"] = username
            return redirect('validation')
            
        # Redirect to a success page.
        else:
            messages.success(request, ("Error de Inicio de Sesion"))
            return redirect('login')
        # Return an 'invalid login' error message.
    else:
        return render(request, "login.html", {})

def validation(request):
    error_message = None
    if request.method == "POST":
        otp = request.POST['otp']
        username = request.session["username"]

        otp_secret_key = request.session['otp_secret_key']
        otp_valid_until = request.session['otp_valid_date']

        if otp_secret_key and otp_valid_until is not None:
            valid_until = datetime.fromisoformat(otp_valid_until)

            if valid_until > datetime.now():
                totp = pyotp.TOTP(otp_secret_key, interval=60)

                if totp.verify(otp):
                    user = get_object_or_404(User, username=username)
                    login(request, user)

                    del request.session['otp_secret_key']
                    del request.session['otp_valid_date']

                    return redirect('home')
                
                else:
                    error_message = 'OTP invalido'
            else:
                error_message = 'OTP ha expirado'
        else:
            error_message = 'Algo salio mal...'

    return render(request, "validation.html", {"error_message": error_message})

@login_required
def home_view(request):

    if 'username' in request.session:
        del request.session['username']
    return render(request, "home.html",{})
