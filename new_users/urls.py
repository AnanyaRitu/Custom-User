from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('registration/', views.registration, name="registration"),
]