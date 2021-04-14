from django.db import models
from direct_messages.models import DirectMessage
from net_user_app.models import NetUser
from notification.models import Notification


def notifications(request):
    if request.user.is_authenticated:
        html = 'notifications.html'
        notes = Notification.objects.filter(
            notified_user=request.user).filter(viewed=False)
        new_notify = DirectMessage.objects.filter(
            id__in=[x.notify.id for x in notes]).order_by(
                "-creation_date")
        for note in notes:
            note.viewed = True
            note.save()
        notified_user = NetUser.objects.get(id=request.user.id)
        return render(request, html, {
            'new_notify': new_notify,
            'notes': notes,
            'user': notified_user})
    return redirect('/login/')
