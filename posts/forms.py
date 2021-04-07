from django import forms

class PostForm(forms.Form):
    header = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea, required=False)