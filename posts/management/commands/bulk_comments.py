from django.core.management.base import BaseCommand
import random
from posts.models import Post
from net_user_app.models import NetUser
from net.models import Net
from mimesis import Text 

text = Text('en')

class Command(BaseCommand):
    help = 'Create bulk amout of users.'

    def handle(self, *args, **kwargs):
        post = Post.objects.all()
        for x in range(100):
            random_index = random.randrange(0, (len(post)))
            author = NetUser.objects.get(id=random.randint(1, NetUser.objects.all().count()))
            parent = post[random_index]
            subnet = parent.subnet
            header = text.title()
            Post.objects.create(
                post_type = 'Comment',
                author = author,
                subnet = subnet,
                header = header,
                parent= parent,
            )
        print("Post are created.")
