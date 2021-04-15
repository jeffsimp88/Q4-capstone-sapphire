from django.db import models
from django.utils import timezone
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey
from net.models import Net
from net_user_app.models import NetUser
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
    post_type = models.CharField(max_length=15, default="Net", choices=POST_CHOICES)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="author", on_delete=models.CASCADE)
    subnet = models.ForeignKey(Net, related_name="subnet", on_delete=models.CASCADE)
    header = models.CharField(max_length=50)
    content = models.TextField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    has_liked = models.ManyToManyField(NetUser, related_name='has_liked', blank=True)
    has_disliked = models.ManyToManyField(NetUser, related_name='has_disliked', blank=True)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children')
    timestamp = models.DateTimeField(default=timezone.now)


    @property
    def total_score(self):
        return (self.upvotes - self.downvotes)

    @property
    def get_comments(self):
        return self.get_children()

    @property
    def root(self):
        return self.get_root()

    @property
    def time_ago(self):
        time = (self.timestamp - timezone.now())
        time_ago = round(time.total_seconds()/3600 *(-1))
        if time_ago > 24:
            time_ago = round(time_ago/24)
            time_ago = f"{time_ago} days ago"
            return time_ago
        elif time_ago <= 1:
            time_ago = f"less than 1 hour ago"
            return time_ago
        else:
            time_ago = f"{time_ago} hours ago"
            return time_ago
    
    def __str__(self):
        return f'{self.header} | {self.author}'

    class MPTTMeta:
        order_insertion_by = ['header']
    

#