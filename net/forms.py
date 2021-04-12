from django import forms
from net.models import Net

IS_PRIVATE = ((False, 'Public'), (True, 'Private'))
class CreateNet(forms.Form):
    title = forms.CharField(max_length=50)
    description = forms.CharField(widget=forms.Textarea, max_length=200)
    rules =forms.CharField(label="Rules(optional)", max_length=200, widget=forms.Textarea, required=False)
    private = forms.ChoiceField(label="Is this Public or Private", choices=IS_PRIVATE, required=False)

class SearchForm(forms.Form):
    search_info = forms.CharField(max_length=50, label="Net Search")
    
class UserSearchForm(forms.Form):
    user_info = forms.CharField(max_length=50, label="User Search")
    

