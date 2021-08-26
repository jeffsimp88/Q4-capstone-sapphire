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
            'profile_image',
            'score',
            'subs',
            'followers',
            'site_theme',
        )


class NetUserUpdateForm(forms.ModelForm):
    """Form for updating user's profile"""
    class Meta:
        model = NetUser
        fields =[
            'username',
            'email',
            'bio',
            'profile_image',
        ]
        

class NetUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = NetUser
        fields = (
            'username',
            'email',
            'bio',
            'profile_image',
            'score',
            'subs',
            'followers', 
            'site_theme',
        )









    # username = forms.CharField(max_length=30)
    # email = forms.EmailField(max_length=100)
    # bio = forms.CharField(widget=forms.Textarea, max_length=250)
    # profile_image = forms.ImageField(required=False)
# class NetUserUpdateForm(forms.Form):
#     username = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=100)
#     bio = forms.CharField(widget=forms.Textarea, max_length=250)
#     profile_image = forms.ImageField(required=False)