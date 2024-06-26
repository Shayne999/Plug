from django.urls import path
from . import views
from .views import DeletePostView

#app_name = 'feed'

urlpatterns = [
    path('', views.feed_view, name='feed'),
    path('upload/', views.upload, name='upload'),
    path('like/<uuid:post_id>/', views.like_post, name='like_post'),
    path('favorites/', views.favorites_view, name='favorites'),
    path('add_to_favorites/<uuid:post_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove_from_favorites/<uuid:post_id>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('upload_page/', views.upload_page, name='upload_page'),
    path('delete_post/<uuid:post_id>/', DeletePostView.as_view(), name='delete_post'),
]
