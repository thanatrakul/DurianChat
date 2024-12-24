from .views import ConversationListView
from django.urls import path

app_name = "facebook_conversations"

urlpatterns = [
    path('<int:contact_id>/', ConversationListView.as_view(), name='conversation_list'),
]
