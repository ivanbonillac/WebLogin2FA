from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('validation/', views.validation, name='validation'),
    path('home/', views.home, name='home'),
    
]