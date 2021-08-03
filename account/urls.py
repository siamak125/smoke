from django.urls import path
from account import views
from account.views import PasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile', views.profileView),
    path('profileRegister', views.profileRegisterView),
    path('logout', views.logoutView),
    path('password', views.change_password),

]
