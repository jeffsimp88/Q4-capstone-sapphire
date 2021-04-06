from django.db import models
from django.utils import timezone
# Create your models here.

# DateTime,
# Content,
# Author,
# Parent(Net, post, comment),
# Upvotes,
# Downvotes,
# Total Votes(method),

class Post(models.Model):
    POST_CHOICES = [
        ("N", "Net"),
        ("P", "Post"),
        ("C", "Comment"),
    ]
    post_type = models.CharField(max_length=1, choices=POST_CHOICES)
    timestamp = models.DateTimeField(timezone.now)
    content = models.TextField(max_length=1000, null=False, blank=False)
    author = models.ForeignKey(
        "CustomUser",
        related_name="author",
        on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    parent = models.ForeignKey("Post", related_name="parent", on_delete=models.CASCADE)


    @property
    def total_score(self):
        self.upvotes - self.downvotes
    
    def __str__(self):
        return self.post_type
