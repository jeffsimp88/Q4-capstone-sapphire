from django import forms
from net.models import Net
from net_user_app.models import NetUser

IS_PRIVATE = ((False, 'Public'), (True, 'Private'))
class CreateNet(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea, max_length=200)
    rules =forms.CharField(label="Rules(optional)", max_length=200, widget=forms.Textarea, required=False)
    private = forms.ChoiceField(label="Is this Public or Private", choices=IS_PRIVATE, required=False)

class SearchForm(forms.Form):
    search_info = forms.CharField(max_length=50, label="", widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    params = forms.CharField(max_length=20, label="", required=False)

class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, member):
        return f"{member.username}"

class ChangeModerators(forms.Form):
    moderators = CustomMMCF(
        queryset=NetUser.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
class ChangeSubscribers(forms.Form):
    subscribers = CustomMMCF(
        queryset=NetUser.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
