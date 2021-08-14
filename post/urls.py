from django.urls import path
from post import views


urlpatterns = [
    path('post', views.Post),


]
