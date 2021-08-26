from notification.models import Notification

def get_notifications(request):
    if request.user.is_authenticated:
        user_notifications = Notification.objects.filter(to_user=request.user)
        return {'notifications': user_notifications.filter(is_read=False)}
    else:
        return {'notifications': []}
