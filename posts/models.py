from django.db import models
from django.utils import timezone
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
from net.models import Net
# Create your models here.

# DateTime,
# Content,
# Author,
# Parent(Net, post, comment),
# Upvotes,
# Downvotes,
# Total Votes(method),

POST_CHOICES = [
    ("Net", "Net"),
    ("Post", "Post"),
    ("Comment", "Comment"),
]


class Post(MPTTModel):
    post_type = models.CharField(max_length=15, choices=POST_CHOICES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="author", on_delete=models.CASCADE)
    subnet = models.ForeignKey(Net, related_name="subnet", on_delete=models.CASCADE)
    header = models.CharField(max_length=50)
    content = models.TextField(max_length=1000, null=True, blank=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    timestamp = models.DateTimeField(default=timezone.now)


    @property
    def total_score(self):
        self.upvotes - self.downvotes
    
    def __str__(self):
        return f'{self.header} | {self.author}'

    class MPTTMeta:
        order_insertion_by = ['header']
