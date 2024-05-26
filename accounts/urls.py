from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sign_up/', views.sign_up, name="sign_up"),
    #path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('home/', views.home, name="home"),
    path('settings/', views.settings, name="settings"),
]