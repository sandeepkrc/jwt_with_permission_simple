from django.conf.urls import url
from django.urls import path, include
from src import views


urlpatterns = [
      path('api/register', views.RegisterApi.as_view()),
      path('hello/', views.HelloView.as_view(), name='hello'),
]