from django.urls import path

from . import views

urlpatterns = [
    path('', views.startup, name='startup'),
    path('home/', views.home, name='home'),
]
