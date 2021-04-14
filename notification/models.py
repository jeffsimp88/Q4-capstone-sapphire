<<<<<<< HEAD
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


=======
# from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
# from direct_messages.models import DirectMessage
# from net_user_app.models import NetUser

# Create your models here.
>>>>>>> c5df4486717bb63c4069dcec2aa0d3c702466381
class Notification(models.Model):
    MESSAGE = 'message'
    APPLICATION = 'application'

    CHOICES = (
<<<<<<< HEAD
        (MESSAGE, 'Message'),
        (APPLICATION, 'Application')
=======
        (MESSAGE, "Message"),
        (APPLICATION, "Application"),
>>>>>>> c5df4486717bb63c4069dcec2aa0d3c702466381
    )

    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']