"""cigarate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include, re_path

from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('login/', views.loginView),
    path('about', views.aboutView, ),
    path('home', views.homeView),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='account/password.html')),
    path('password-reset', views.passwordReset, name="password-reset"),
    # re_path(r'password-reset/(?P<havij>[\w]{32})/', views.passwordReset2),
    path('password-reset/<uuid:rock>/', views.passwordReset2),
    path('password-reset/<path:id>/', views.passwordReset),
    path('password-reset', views.passwordReset),
]
