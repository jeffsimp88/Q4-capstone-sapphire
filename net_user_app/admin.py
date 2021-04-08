from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from net_user_app.models import NetUser
from net_user_app.forms import NetUserForm, NetUserChangeForm

# Register your models here.
# admin.site.register(NetUser)

class NetUserAdmin(UserAdmin):
    add_form = NetUserForm
    form = NetUserChangeForm
    model = NetUser
    list_display = (
        'username',
        'email',
        'score',
        'is_staff',
        'is_active',
        )
    list_filter = (
        'is_staff',
        'is_active',
        )
    fieldsets = (
        (None, {'fields': (
            'username',
            'email',
            'bio',
            'score',
            'subs',
            'followers',
            'password',            
            'site_theme',
            
                
            )}),('Permissions', {'fields': ('is_staff', 'is_active')})
    )
    
    add_fieldsets = (
        (None, {
            'classes':('wide',),
            'fields': (
            'username',
            'email',
            'bio',
            'score',
            'subs',
            'followers',
            'site_theme',
            'password1',
            'password2',
            'is_staff', 
            'is_active',
            ),},),)

admin.site.register(NetUser, NetUserAdmin)