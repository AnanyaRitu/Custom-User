from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('registration/', views.registration, name="registration"),
    path('fa_dash/', views.FA_dash, name="fa_dash"),
    path('ic_dash/', views.IC_dash, name="ic_dash"),
]
