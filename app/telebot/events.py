from time import time
from flask import session, request
from flask_socketio import emit, join_room, leave_room
from flask_socketio import SocketIO

socketio = SocketIO()

users = {}

@socketio.on('test', namespace='/telebot/chats')
def test(message):
    print(f"test: {message}")
    emit("response", {"data": "test response"}, to=request.sid)
    
@socketio.on('connect', namespace='/telebot/chats')
def connect():
    print(f"connect: {request.sid}")
    users[request.sid] = {"time": time()}
    emit("response", {"data": "connected"}, to=request.sid)
    
@socketio.on('disconnect', namespace='/telebot/chats')
def disconnect():
    print(f"disconnect: {request.sid}")
    users.pop(request.sid, None)
    emit("response", {"data": "disconnected"}, to=request.sid)
    

