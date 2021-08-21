from django.urls import path
from post import views


urlpatterns = [
    path('post', views.PostAPIView.as_view()),
    # path('post/<int:id>', views.PostRetrieveUpdateDestroyView.as_view()),


]
