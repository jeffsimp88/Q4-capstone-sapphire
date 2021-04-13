from django import Modelform
from .models import DirectMessage


class DirectMessageForm(Modelform):
    class Meta:
        model = DirectMessage
        fields = ['msg_content']
