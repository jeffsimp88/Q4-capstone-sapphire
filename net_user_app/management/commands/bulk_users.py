from django.core.management.base import BaseCommand
from net_user_app.models import NetUser
from mimesis import Person, Text


person = Person('en')

text = Text('en')
class Command(BaseCommand):
    help = 'Create bulk amout of users.'

    def handle(self, *args, **kwargs):
        for x in range(20):
            username = person.username()
            password = person.password()
            email = person.email()
            bio = text.sentence()
            NetUser.objects.create(
            username = username,
            password = password,
            email = email,
            bio = bio,
            )
        print("Users are created.")
