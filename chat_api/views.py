import json

import websocket

from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.shortcuts import HttpResponse



def index(request):
    return render(request, 'chat_api/index.html')

def room(request, room_name):
    return render(request, 'chat_api/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def chat_send(request, room_name):
    if request.method == 'GET':
        import pdb; pdb.set_trace()
        host = request.get_host()
        ws = websocket.WebSocket()
        ws.connect("ws://{}/ws/chat/{}/".format(host, room_name))
        # ws = websocket.WebSocket("ws://{}/ws/chat/{}/".format(host, room_name))

        send_msg = {"message":"inner method call()"}
        res = ws.send(json.dumps(send_msg))

        return HttpResponse(status=200, content="test success - " + room_name)

def chat_list(request, room_name):
    if request.method == 'GET':
        import pdb; pdb.set_trace()
        host = request.get_host()
        ws = websocket.WebSocket()
        ws.connect("ws://{}/ws/chat/{}/".format(host, room_name))
        # ws = websocket.WebSocket("ws://{}/ws/chat/{}/".format(host, room_name))

        res = ws.recv()
        print("=============")
        print(res)

        return HttpResponse(status=200, content="test success - " + room_name)