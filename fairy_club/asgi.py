import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fairy_club.settings')
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import fairy_club.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),

    "websocket": AuthMiddlewareStack(
        URLRouter(
            fairy_club.routing.websocket_urlpatterns
        )
    ),
})
