from django.db import models
from django.contrib.auth.models import AbstractUser
from net.models import Net

LIGHT_DARK = (('Light', 'Light'), ('Dark', 'Dark'))

class NetUser(AbstractUser):
    email = models.EmailField(max_length=100)
    bio = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/', null=True, blank=True)
    score = models.IntegerField(default= 0)
    subs = models.ManyToManyField(Net, related_name="subs", blank=True)
    followers = models.ManyToManyField('NetUser')
    site_theme = models.CharField(choices=LIGHT_DARK, max_length=10, default='Light', null=True, blank=True)
    


    
