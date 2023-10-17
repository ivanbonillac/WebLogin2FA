import pyotp
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.core.mail import send_mail

def send_otp(request):
    #creating the OTP
    totp = pyotp.TOTP(pyotp.random_base32(), interval=60)
    otp = totp.now()
    request.session['otp_secret_key'] = totp.secret
    valid_date = datetime.now() + timedelta(minutes=1)
    request.session['otp_valid_date'] = str(valid_date)

    #send otp via terminal
    print(f"Verification code: {otp}")

    send_mail(
        "Alerta Inicio de Sesion",#Asunto
        f"Su codigo es: {otp}",#Cuerpo
        "ivandeveloper28@gmail.com",#email enviante
        ["ivan.bonilla@utp.ac.pa", "iandresb28@icloud.com"],#email receptor
    )   
    




