import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)

        if 'typing' in data:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'typing_status',
                    'username': data.get('username', 'Anonymous'),
                    'typing': data['typing']
                }
            )
            return

        username = data.get('username', 'Anonymous')
        message = data.get('message')
        image = data.get('image',None)  # base64 string

        await self.save_message(self.room_name, username, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'username': username,
                'message': message,
                'image': image
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps({
            'username': event['username'],
            'message': event['message'],
            'image': event.get('image')
        }))

    async def typing_status(self, event):
        await self.send(text_data=json.dumps({
            'username': event['username'],
            'typing': event['typing']
        }))

    @sync_to_async
    def save_message(self, room, username, message):
        Message.objects.create(room=room, username=username, content=message)
