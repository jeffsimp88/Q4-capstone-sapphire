from django import forms
from notification.models import Notification

class CreateNotification(forms.ModelForm):
    class Meta:
        model = Notification
        fields = [
            'to_user',
            'notification_type',
            'is_read',
            'post_comment',
            'subnet',
            'created_by',
            ]