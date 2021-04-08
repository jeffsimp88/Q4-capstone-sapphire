from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from net_user_app.models import NetUser

class NetUserForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = NetUser
        fields = (
            'username',
            'email',
            'bio',
            'score',
            'subs',
            'followers',
            'site_theme',
        )
        

class NetUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = NetUser
        fields = (
            'username',
            'email',
            'bio',
            'score',
            'subs',
            'followers', 
            'site_theme',
        )