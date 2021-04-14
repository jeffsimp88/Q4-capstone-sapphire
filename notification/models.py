from django.db import models
from direct_messages.models import DirectMessage
from net_user_app.models import NetUser

# Create your models here.
class Notification(models.Model):
    notify = models.ForeignKey(DirectMessage, on_delete=models.CASCADE)
    notified_user = models.ForeignKey(NetUser, on_delete=models.CASCADE)
    viewed = models.BooleanField(
        default=False
    )

    def __str__(self):
        return "Notification about " + self.notify.notify