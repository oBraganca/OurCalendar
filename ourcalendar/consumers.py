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
        idcalendar= OurCalendar.objects.get(id=idcalendar)
        Events.objects.create(
            name=title,
            description=description,
            date_start=date_start,
            date_end=date_end,
            calendar=idcalendar,
            origim=idcalendar,

        )
