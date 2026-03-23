import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'test'
        #first parameter is an async function (channels))
        async_to_sync(self.channel_layer.group_add)(
            #the function
            self.room_group_name,
            self.channel_name
        )
        self.accept()
    def disconnect(self, close_code):
         #first parameter is an async function (channels))
        async_to_sync(self.channel_layer.group_discard)( 
             #the function
            self.room_group_name, self.channel_name)

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        #first parameter is an async function (channels)
        async_to_sync(self.channel_layer.group_send)(
            #the function
            self.room_group_name,{
                'type':'chat_message',
                'message':message
            }
        )
    def chat_message(self, event):
        message = event['message']
        #send a message to the client
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))