from django.urls import path
from login import consumers

websocket_urlpatterns = [
    path('ws/mails/', consumers.MailConsumer.as_asgi()),
]
