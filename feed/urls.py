from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('upload/', views.upload, name='upload'),
    path('like-post/', views.like_post, name='like-post'),

]