from django.db import models
from django.contrib.auth.models import AbstractUser
from net.models import Net


class NetUser(AbstractUser):
    email = models.EmailField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    score = models.IntegerField(default = 0)
    subs = models.ManyToManyField(Net, related_name="subs", null=True, blank=True)
    followers = models.ManyToManyField("NetUser")
    


    
