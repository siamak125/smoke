from django.urls import path
from post import views


urlpatterns = [
    path('post', views.PostAPIView.as_view(), name='post'),
    # path('post/<int:id>', views.PostRetrieveUpdateDestroyView.as_view()),


]
