import json

from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from channels.layers import get_channel_layer
from ourcalendar.models import *
import _thread
channel_layer = get_channel_layer()

class CalendarConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'Calendar'
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        data = json.loads(text_data)
        title = data['title']
        description = data['description']
        date_start = data['date_start']
        date_end = data['date_end']
        access = data['access']
        idcalendar = data['idcalendar']
        
        self.save_message(title, description, date_start, date_end, access, idcalendar),
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'calendar_message',
                'title': title,
                'description': description,
                'date_start': date_start,
                'date_end': date_end,
                'access': access
            },
        )
        
    def calendar_message(self, data):
        title = data['title']
        description = data['description']
        date_start = data['date_start']
        date_end = data['date_end']
        access = data['access']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'title': title,
            # 'description': description,
            'start': date_start,
            'end': date_end,
            # 'access': access
        }))
    
    def save_message(self, title, description, date_start, date_end, access, idcalendar):
        print('aaaaaaaaaaa')
        idcalendar= OurCalendar.objects.get(id=idcalendar)
        Events.objects.create(
            name=title,
            description=description,
            date_start=date_start,
            date_end=date_end,
            calendar=idcalendar,
            origim=idcalendar,

        )

# class CalendarConsumer(WebsocketConsumer):
#     async def connect(self):
        
#         self.room_group_name = 'Calendar'
#         await self.accept()

#         self.send(text_data=json.dumps({
#             'type':'Connection_Established',
#             'message':'You are now connected'
#         }))
        
#     async def disconnect(self, code):
#         print("Disconnected", code)
        
        
#     async def receive(self, text_data):
#         data = json.loads(text_data)
        
        
#         title = data['title']
#         description = data['description']
#         date_start = data['date_start']
#         date_end = data['date_end']
#         access = data['access']
#         idcalendar = data['idcalendar']
#         print("Received", title, description, date_start, date_end)

#         # await self.save_message(title, description, date_start, date_end, access, idcalendar)

#         # # Send message to room group
#         # await self.channel_layer.group_send(
#         #     self.calendar_group_name,
#         #     {
#         #         'title': title,
#         #         'description': description,
#         #         'date_start': date_start,
#         #         'date_end': date_end,
#         #         'access': access,
#         #         'idcalendar': idcalendar
#         #     }
#         # )
        
#         await self.send(text_data=json.dumps({
#             'title': title,
#                 'description': description,
#                 'date_start': date_start,
#                 'date_end': date_end,
#                 'access': access
#         }))
        
# class ChatConsumer(WebsocketConsumer):
#     def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_%s' % self.room_name

#         # Join room group
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         self.accept()

#     def disconnect(self, close_code):
#         # Leave room group
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )

#     # Receive message from WebSocket
#     def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         # Send message to room group
#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 'type': 'chat_message',
#                 'message': message
#             }
#         )

#     # Receive message from room group
#     def chat_message(self, event):
#         message = event['message']

#         # Send message to WebSocket
#         self.send(text_data=json.dumps({
#             'message': message
#         }))
