from .views import FBWebhookView
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

app_name = "webhooks"

urlpatterns = [
    path('fb_chats/', csrf_exempt(FBWebhookView.as_view()), name='fb_chat'),
]
