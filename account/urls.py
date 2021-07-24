from django.urls import path
from account import views

urlpatterns = [
    path('login', views.loginView),
    path('help', views.profileView),
    path('profileRegister', views.profileRegisterView)
]
