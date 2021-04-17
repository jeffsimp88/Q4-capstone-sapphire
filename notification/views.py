from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Notification


@login_required
def notifications(request):
    context ={}
    user_notification = Notification.objects.filter(to_user=request.user) 
    context.update({"user_notifications": user_notification})
    return render(request, 'notifications.html', context)

def create_comment_notification(request, post):
    Notification.objects.create(
        to_user=post.author,
        notification_type="Post",
        created_by=request.user,
        post_comment=post,
        subnet = post.subnet
        )

def create_subnet_notifications(request, subnet, post):
    moderators = subnet.moderators.all()
    for mod in moderators:
        Notification.objects.create(
            to_user=mod,
            notification_type="Subnet",
            created_by=request.user,
            post_comment = post,
            subnet=subnet,
        )

def mark_as_read(request):
    user_notifications = Notification.objects.filter(to_user=request.user)
    unread_notifications = user_notifications.filter(is_read = False)
    for notif in unread_notifications:
        notif.is_read = True
        notif.save()
    return redirect("/notifications/")