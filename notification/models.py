from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from posts.models import Post


class Notification(models.Model):

    CHOICES = (
        ('MESSAGE', 'Message'),
        ('APPLICATION', 'Application')
    )

    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES, default='MESSAGE')
    is_read = models.BooleanField(default=False)
    post_comment = models.ForeignKey(Post, related_name='post', on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'notification to {self.to_user} from {self.created_by}'