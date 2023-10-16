from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('validation/', views.validation, name='validation'),
    path('home/', views.home_view, name='home'),
    
]