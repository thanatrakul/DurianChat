import json

from channels.generic.websocket import AsyncWebsocketConsumer

class LiveChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """Handle WebSocket connection."""
        self.page_id = self.scope['url_route']['kwargs']['page_id']
        self.group_name = f"live_chat_{self.page_id}"

        # Join WebSocket group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        """Handle WebSocket disconnection."""
        # Leave WebSocket group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """Handle messages received from WebSocket."""
        data = json.loads(text_data)
        message = data.get('message', '')

        # Broadcast message to WebSocket group
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chat_message",
                "message": message
            }
        )

    async def chat_message(self, event):
        """Handle messages broadcast to WebSocket group."""
        await self.send(text_data=json.dumps({
            "message": event["message"]
        }))
