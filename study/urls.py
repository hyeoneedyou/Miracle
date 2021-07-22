from django.contrib import admin
from django.urls import path
from . import views

app_name = 'study'
urlpatterns = [
    path('', views.main, name="main"),
    path('add_goal/', views.add_goal, name="add_goal"),
    path('certify/', views.certify, name="certify"),
]
