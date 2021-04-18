from django.contrib import admin
from .models import Notification
from notification.forms import CreateNotification



def mark_read(modeladmin, request, queryset):
    queryset.update(is_read=True)
mark_read.short_description = "Mark selected as read"

def mark_unread(modeladmin, request, queryset):
    queryset.update(is_read=False)
mark_unread.short_description = "Mark selected as unread"


class NotificationAdmin(admin.ModelAdmin):
    add_form = CreateNotification
    model = Notification
    list_display = (
        'to_user',
        'notification_type',
        'is_read',
        'post_comment',
        'subnet',
        'created_at',
        'created_by',
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
    actions = [mark_read, mark_unread,]

admin.site.register(Notification, NotificationAdmin)
