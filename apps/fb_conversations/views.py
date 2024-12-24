from .models import Conversation
from django.views.generic import ListView


class ConversationListView(ListView):
    model = Conversation
    template_name = 'conversations/conversation_list.html'
    context_object_name = 'conversations'

    def get_queryset(self):
        contact_id = self.kwargs.get('contact_id')
        return Conversation.objects.filter(contact__id=contact_id).order_by('-timestamp')
