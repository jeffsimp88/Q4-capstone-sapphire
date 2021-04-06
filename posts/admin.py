from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from posts.models import Post
# Register your models here.

admin.site.register(Post, DraggableMPTTAdmin)
