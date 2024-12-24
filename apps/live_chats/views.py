from apps.contacts.models import Contact
from apps.fb_conversations.models import Conversation
from apps.fb_pages.models import FacebookPage
from django.http import JsonResponse
from django.views.generic import ListView
from django.views.generic import View


class LiveChatView(ListView):
    model = Contact
    template_name = "live_chats/live_chat.html"
    context_object_name = "contacts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page = FacebookPage.objects.filter(is_active=True).first()
        context["contacts"] = Contact.objects.all().values('id', 'name', 'last_message', 'profile_picture')
        context["fb_page"] = page
        context["active_menu"] = "live_chats"
        return context


class ConversationAPI(View):
    def get(self, request, contact_id):
        conversations = Conversation.objects.filter(contact_id=contact_id)
        data = [
            {
                "message": conv.message,
                "direction": conv.direction
            } for conv in conversations
        ]
        return JsonResponse({"conversations": data})
