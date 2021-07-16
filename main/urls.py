from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.main_logout, name="main_logout"),
    path('login/', views.main_login, name="main_login"),
]
