import json

from apps.contacts.models import Contact
from apps.fb_conversations.models import Conversation
from apps.fb_pages.models import FacebookPage
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.http import JsonResponse
from django.utils.timezone import now
from django.views import View


class FBWebhookView(View):
    verify_token = 'durian-chat'

    def get(self, request, *args, **kwargs):
        hub_mode = request.GET.get('hub.mode')
        verify_token = request.GET.get('hub.verify_token')
        challenge = request.GET.get('hub.challenge')

        if hub_mode == 'subscribe' and verify_token == self.verify_token:
            return HttpResponse(challenge)
        return HttpResponseForbidden("Invalid verify token.")

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            entry = data.get('entry', [])
            channel_layer = get_channel_layer()

            for item in entry:
                messaging_events = item.get('messaging', [])
                for event in messaging_events:
                    sender_id = event.get('sender', {}).get('id')
                    recipient_id = event.get('recipient', {}).get('id')
                    message_text = event.get('message', {}).get('text', '')

                    if not sender_id or not recipient_id:
                        continue

                    try:
                        fb_page = FacebookPage.objects.get(page_id=recipient_id)
                        contact, _ = Contact.objects.update_or_create(
                            user_id=sender_id,
                            page=fb_page,
                            defaults={
                                'name': "Unknown",
                                'last_message': message_text,
                                'last_contacted': now()
                            }
                        )
                        conversation = Conversation.objects.create(
                            contact=contact,
                            message=message_text,
                            direction='inbound'
                        )

                        async_to_sync(channel_layer.group_send)(
                            "live_chat_group",
                            {
                                "type": "chat_message",
                                "message": {
                                    "contact_id": contact.id,
                                    "contact_name": contact.name,
                                    "message": message_text,
                                    "timestamp": conversation.timestamp.isoformat(),
                                }
                            }
                        )
                    except FacebookPage.DoesNotExist:
                        continue

            return JsonResponse({'status': 'success'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
