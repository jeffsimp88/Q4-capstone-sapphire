from django.contrib import admin
from direct_messages.models import DirectMessage
from direct_messages.forms import DirectMessageForm

class DirectMessageAdmin(admin.ModelAdmin):
    add_form = DirectMessageForm
    model = DirectMessage
    list_display = (
        'sender',
        'reciever',
        'created_at',
        'msg_content',
        )

    fieldsets = (
        (None, {
            "fields": list_display,
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide'), 
            'fields': list_display,
        },),)
    ordering = list_display

admin.site.register(DirectMessage, DirectMessageAdmin)
