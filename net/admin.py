from django.contrib import admin
from net.models import Net
from net.forms import CreateNet

# admin.site.register(Net)

class NetAdmin(admin.ModelAdmin):
    add_form = CreateNet
    model = Net
    list_display = (
        'title',
        'creation_date',
        'private',
        )
    list_filter=(
        'private',
        )
    fieldsets = (
        (None, {
            "fields": ('title', 'description', 'rules', 'moderators', 'creation_date', 'private'),
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide'), 
            'fields': ('title', 'description', 'rules', 'moderators', 'creation_date', 'private'),
        }),
    )
    ordering = (
        'title',
        'creation_date',
        'private',
        )

admin.site.register(Net, NetAdmin)

