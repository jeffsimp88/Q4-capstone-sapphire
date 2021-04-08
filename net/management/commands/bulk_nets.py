from django.core.management.base import BaseCommand
from net.models import Net
from mimesis import Text 

text = Text('en')

class Command(BaseCommand):
    help = 'Create bulk amout of users.'

    def handle(self, *args, **kwargs):
        index = 1
        while index <= 20:
            title = text.word()
            description = text.text(quantity=3)
            rules = text.text(quantity=3)
            if Net.objects.filter(title=title).exists():
                return
            else:
                Net.objects.create(
                    title = title,
                    description = description,
                    rules = rules,
                )
                index += 1
        print("Nets are created.")
