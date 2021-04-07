from django.core.management.base import BaseCommand
from net.models import Net
from mimesis import Text 

text = Text('en')

class Command(BaseCommand):
    help = 'Create bulk amout of users.'

    def handle(self, *args, **kwargs):
        for x in range(20):
            title = text.word()
            description = text.text(quantity=3)
            rules = text.text(quantity=3)
            Net.objects.create(
                title = title,
                description = description,
                rules = rules,
            )
        print("Nets are created.")
