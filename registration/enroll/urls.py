from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name = 'Home'),
    path('register',views.register,name ="Register"),
    path('login', views.loggin, name ="Login"),
    path('logout', views.loggout, name ="Logout"),



]
