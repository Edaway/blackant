from flask_socketio import emit, join_room, leave_room
from flask_login import current_user
from .. import socketio

@socketio.on('join')
def handle_join(data):
    room = data.get('room')
    if room:
        join_room(room)
        emit('message', {'user': 'Система', 'msg': f'{current_user.username} вошел в комнату.'}, to=room)

@socketio.on('leave')
def handle_leave(data):
    room = data.get('room')
    if room:
        leave_room(room)
        emit('message', {'user': 'Система', 'msg': f'{current_user.username} покинул комнату.'}, to=room)

@socketio.on('send_message')
def handle_send_message(data):
    room = data.get('room')
    msg = data.get('msg')
    if room and msg:
        emit('message', {'user': current_user.username, 'msg': msg}, to=room)
