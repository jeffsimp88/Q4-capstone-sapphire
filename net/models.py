from django.db import models
from django.utils import timezone
from django.conf import settings



class Net(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, unique=True)
    description = models.TextField(null=False, blank=False)
    rules = models.TextField(null=True, blank=True)
    moderators = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="moderators")
    creation_date = models.DateTimeField(default=timezone.now)
    private = models.BooleanField(default=False)
    subscribers = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    
