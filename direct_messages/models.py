from django.db import models
from net_user_app.models import NetUser
from django.utils import timezone

# Create your models here.


class DirectMessage(models.Model):
    sender = models.ForeignKey(NetUser, related_name="sender", on_delete=models.CASCADE)
    reciever = models.ForeignKey(NetUser, related_name="reciever", on_delete=models.CASCADE)
    msg_content = models.TextField(max_length=1000,)
    created_at = models.DateTimeField(default=timezone.now)
