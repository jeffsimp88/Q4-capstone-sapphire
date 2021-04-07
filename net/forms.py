from django import forms

class Create_Net(forms.Form):
    title = forms.Charfield(widget=forms.Textarea)
    content = forms.Charfield(widget=forms.Textarea)
    

