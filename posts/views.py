from django.shortcuts import render
from posts.forms import PostForm
from posts.models import Post

def post_form_view(request):
    if request.method == 'POST':
        print("It's a post!")
    form = PostForm()
    context = {'form': form}
    return render(request, "forms.html", context)
