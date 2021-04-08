from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from posts.models import Post
from posts.forms import PostForm

admin.site.register(
    Post, 
    DraggableMPTTAdmin,
    list_display = (
        "tree_actions",
        'indented_title',
        'author',
        'post_type',
        'subnet',
        'timestamp',
        ),
    list_display_links=('indented_title',),
    list_filter = ('post_type', 'author','subnet',),
    )