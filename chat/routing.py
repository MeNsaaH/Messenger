from django.urls import path

from . import consumer

websocket_urlpatterns = [
    path(r'ws/chat/<str:room_name>/', consumer.ChatConsumer)
]
