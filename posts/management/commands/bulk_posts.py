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
        subnets = Net.objects.all()
        for x in range(100):
            author = NetUser.objects.get(id=random.randint(1, NetUser.objects.all().count()))
            subnet = subnets[random.randint(1, (len(subnets)+1))]
            header = text.title()
            content = text.text(quantity=4)
            Post.objects.create(
                post_type = 'Post',
                author = author,
                subnet = subnet,
                header = header,
                content = content,
            )
        print("Post are created.")
