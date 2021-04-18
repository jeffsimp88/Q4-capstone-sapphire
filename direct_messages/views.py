from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from itertools import chain
from direct_messages.models import DirectMessage
from direct_messages.forms import DirectMessageForm
from net_user_app.models import NetUser

@login_required
def message_view(request):
    messages = DirectMessage.objects.filter(reciever=request.user)
    sent_messages = DirectMessage.objects.filter(sender=request.user)
    context = {'messages': messages, 'sent_messages': sent_messages}
    return render(request, 'messages.html', context)

@login_required
def user_message_view(request, username):
    reciever_user = NetUser.objects.get(username=username)
    current_user = request.user
    recieved_messages = DirectMessage.objects.filter(reciever=reciever_user)
    recieved_messages = recieved_messages.filter(sender=current_user)
    sent_messages = DirectMessage.objects.filter(reciever=current_user)
    sent_messages = sent_messages.filter(sender=reciever_user)
    messages = sorted(chain(recieved_messages, sent_messages), key=lambda data: data.created_at, reverse=True)
    if request.method == 'POST':
        form = DirectMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_message = DirectMessage.objects.create(
                sender = current_user,
                reciever = reciever_user,
                msg_content = data['msg_content'],
            )
            return HttpResponseRedirect(f'/messages/{reciever_user.username}/')
    message_form = DirectMessageForm()
    context={'messages': messages, 'message_form':message_form}
    return render(request, 'user_messages.html', context)


@login_required
def create_message(request, username):
    reciever_user = NetUser.objects.get(username=username)
    if request.method == 'POST':
        form = DirectMessageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_message = DirectMessage.objects.create(
                sender = request.user,
                reciever = reciever_user,
                msg_content = data['msg_content'],
            )
            return HttpResponseRedirect(f'/users/{reciever_user.username}/')

