from django.db import models
from django.utils import timezone
from django.conf import settings
from django.apps import apps



class Net(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    rules = models.TextField(null=True, blank=True)
    moderators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="moderators")
    creation_date = models.DateTimeField(default=timezone.now)
    private = models.BooleanField(default=False)
    subscribers = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.title

    @property
    def total_subscribers(self):
        users = apps.get_model('net_user_app', 'Netuser')
        return len(users.objects.filter(subs__title=self.title))

    
