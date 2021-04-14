from .models import Notification

<<<<<<< HEAD
def notifications(request):
    if request.user.is_authenticated:
        return {'notifications': request.user.notifications.filter(is_read=False)}
    else:
        return {'notifications': []}
=======
def notification(request):
    if request.user.is_authenticated:
        return {'notification': request.user.notifications.filter(is_read=False)}
    else:
        return {'notification': []}
>>>>>>> c5df4486717bb63c4069dcec2aa0d3c702466381
