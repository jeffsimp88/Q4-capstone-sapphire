from django.shortcuts import render
from posts.forms import PostForm, CommentForm
from posts.models import Post

def post_comment_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_post = Post.objects.create(
                header = data['header'],
                author = request.user,
                post_type = 'Comment',
                parent = post,
                subnet = post.subnet
            )
    form = CommentForm()
    context = {'form': form}
    return render(request, "forms.html", context)
