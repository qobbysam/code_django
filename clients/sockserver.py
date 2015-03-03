import os
import tornado.httpserver
import tornado.wsgi
import sys
import django.core.handlers.wsgi

sys.path.append('/home/ubuntu/clients')


import json
from sockjs.tornado import SockJSConnection
from clients.models import  MyClient


class ChatConnection(SockJSConnection):
    _connected = set()

    def on_open(self, request):                                 #This is Defining how the open will be handled
        #print "OPEN"
        #print request.get_cookie('name')
        self._connected.add(self)
        for each in MyClient.objects.all().order_by('onSending')[:10]:
            self.send(self._package_message(each))

    def on_message(self, data):                                   #This is defining how the messages will be handled when recieved
        data = json.loads(data)
        #print "DATA", repr(data)
        msg = MyClient.objects.create(
            username=data['username'],
            message=data['message'],
            codeJava = data['codeJava'],
            codePython =data['codePython'],
        )
        self.broadcast(self._connected, self._package_message(msg))

    def on_close(self):
        #print "CLOSE"
        self._connected.remove(self)

    def _package_message(self, m):
        return {'onSending': m.onSending.strftime('%H:%M:%S'),
                'message': m.message,
                'username': m.username,
                'codeJava': m.codeJava,
                'codePython' : m.codePython,}

if __name__ == "__main__":
    main()
