from django.urls import path
from .views import chat, ListThreads, CreateThread, ThreadView, CreateMessage, ThreadNotification

urlpatterns = [
    path('', chat, name='chat'),
    path('inbox/', ListThreads.as_view(), name='inbox'),
    path('create-thread/', CreateThread.as_view(), name='create-thread'),
    path('inbox/<int:pk>/', ThreadView.as_view(), name='thread'),
    path('inbox/<int:pk>/create-message/', CreateMessage.as_view(), name='create-message'),
    # path('notification/int:pk>/thread/int.object_pk>/', ThreadNotification.as_view(), name='thread-notifications'),
    path('notification/<int:notification_pk>/thread/<int:object_pk>/', ThreadNotification.as_view(), name='thread-notifications'),
]