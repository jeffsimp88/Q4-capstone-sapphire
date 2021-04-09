from django import forms
from posts.models import Post

class PostForm(forms.Form):
    header = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea, required=False)

class PostImage(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'header',
            'image',
        )

class CommentForm(forms.Form):
    header = forms.CharField(max_length=50, label="Comment")