from django.urls import path
from post import views

urlpatterns = [
    path('post', views.PostAPIView.as_view(), name='post'),
    path('like/', views.like, name='like_post'),
]
