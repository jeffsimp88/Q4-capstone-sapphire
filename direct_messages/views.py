from django.shortcuts import render
from direct_messages.models import DirectMessage
from direct_messages.forms import DirectMessageForm

def message_view(request):
    messages = DirectMessage.objects.filter(reciever=request.user)

    context = {'messages': messages}
    return render(request, 'messages.html', context)
