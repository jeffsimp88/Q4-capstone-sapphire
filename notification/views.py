from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification


@login_required

def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)
    extra_id = request.GET.get('extra_id', 0)
    user_notification = Notification.objects.filter(to_user=request.user)
    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.MESSAGE:
            return redirect('view_application', application_id=notification.extra_id)
        elif notification.notification_type == Notification.APPLICATION:
            return redirect('view_application', application_id=notification.extra_id)

    return render(request, 'notifications.html', {"notifications": user_notification})

def create_notification(request, post):
    Notification.objects.create(
        to_user=post.author,
        notification_type="MESSAGE",
        created_by=request.user,
        post_comment=post,
        )