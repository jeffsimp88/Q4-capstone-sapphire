from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL
from posts.models import Post
from net.models import Net


class Notification(models.Model):

    CHOICES = (
        ('Post', 'Post'),
        ('Subnet', 'Subnet')
    )

    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES, default='Post')
    is_read = models.BooleanField(default=False)
    post_comment = models.ForeignKey(Post, related_name='notified_post', on_delete=models.CASCADE, null=True, blank=True)
    subnet = models.ForeignKey(Net, related_name='notified_subnet', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'notification to {self.to_user} from {self.created_by}'