<<<<<<< HEAD
from .models import Notification
=======
from . models import Notification
>>>>>>> c5df4486717bb63c4069dcec2aa0d3c702466381

def create_notification(request, to_user, notification_type, extra_id=0):
    notification = Notification.objects.create(to_user=to_user, notification_type=notification_type, created_by=request.user, extra_id=extra_id)