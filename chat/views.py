from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message
from .crypto import decrypt_message

def index(request):
    return render(request, "chat/index.html")


@login_required
def room(request, room_name):
    qs = Message.objects.filter(room=room_name).order_by('timestamp')[:50]

    # Decrypt stored message contents for display. We build a small list of
    # dicts rather than passing model instances because content in the DB is
    # stored encrypted (base64 nonce+ciphertext).
    messages = []
    for m in qs:
        messages.append({
            'username': m.username,
            'message': decrypt_message(m.content),
            'timestamp': m.timestamp,
        })

    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages
    })