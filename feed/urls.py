from django.urls import path
from . import views

#app_name = 'feed'

urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('upload/', views.upload, name='upload'),
    path('like/<uuid:post_id>/', views.like_post, name='like_post'),
]