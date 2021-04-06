from django.db import models
from django.utils import timezone


class Net(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    rules = models.TextField(null=True, blank=True)
    moderators = models.ManyToManyField(
        "CustomUser",
        related_name="moderators")
    creation_date = models.DateTimeField(timezone.now)
    private = models.BooleanField(default=False)

    __str__(self):
        return self.title
