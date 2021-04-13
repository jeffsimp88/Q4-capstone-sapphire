from django.db import models
from net_user_app.models import NetUser

# Create your models here.


class DirectMessage(models.Model):
    sender = models.ForeignKey(NetUser, related_name="sender")
    reciever = models.ForeignKey(NetUser, related_name="reciever")
    msg_content = models.TextField(max_length=1000, related_name="content")
    created_at = models.TimeField(auto_now=True, auto_now_add=True)
