from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sign_up/', views.sign_up, name="sign_up"),
    path('logout/', views.logout, name="logout"),
    path('home/', views.home, name="home"),
    path('settings/', views.settings, name="settings"),
    path('chat/', views.chat, name="chat"),
    path('connections/', views.connections, name="connections"),
    path('settings/delete/', views.delete_profile_view, name='delete_profile'),
]