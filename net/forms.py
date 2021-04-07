from django import forms
from net.models import Net

class Create_Net(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    
    

