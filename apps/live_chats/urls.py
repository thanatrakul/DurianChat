from .views import ConversationAPI
from .views import LiveChatView
from django.urls import path

app_name = "live_chats"


urlpatterns = [
    path("home/", LiveChatView.as_view(), name="home"),
    path("conversation/<int:contact_id>/", ConversationAPI.as_view(), name="conversation-api"),
]
