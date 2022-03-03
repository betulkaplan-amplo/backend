import json
from channels.generic.websocket import WebsocketConsumer
from threading import Timer

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

        def delayed_message():
            self.send(text_data=json.dumps({
                'type':'connection established',
                'message':'You are now connected!',
            }))

        

        t = Timer(5, delayed_message)  
        t.start()