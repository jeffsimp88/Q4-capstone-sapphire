from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from posts.forms import PostForm, CommentForm, PostImage
from posts.models import Post
from net.models import Net
from net.views import search_net, search_user
from net.forms import UserSearchForm, SearchForm

def individual_post_view(request, post_id):
    context = {'header': "Post Details"}
    post = Post.objects.get(id=post_id)
    comments = Post.objects.filter(parent=post).order_by('timestamp')
    root_post = post.get_root()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            new_post = Post.objects.create(
                header = data['header'],
                author = request.user,
                post_type = 'Comment',
                parent = post,
                subnet = post.subnet
            )
            return redirect(f"/posts/{root_post.id}/")
    comment_form = CommentForm()
    comment_form.fields['header'].label = ""
    context.update({'post': post, 'comments': comments, 'comment_form': comment_form,})
    return render(request, 'individual_posts.html', context)

@login_required
def create_post_view(request, net_title):
    context = {'header': "Post a Post"}
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subnet = Net.objects.get(title=net_title)
            new_post = Post.objects.create(
                post_type = 'Post',
                author = request.user,
                subnet = subnet,
                header = data['header'],
                content = data['content'],
            )
            return HttpResponseRedirect(f'/nets/{net_title}')

@login_required
def post_image_view(request, net_title):
    context = {'header': "Post an Image"}
    user = request.user
    if request.method == 'POST':
        form = PostImage(request.POST, request.FILES, instance=user)
        if form.is_valid():
            data = form.cleaned_data
            subnet = Net.objects.get(title=net_title)
            new_post = Post.objects.create(
                post_type = 'Post',
                author = user,
                subnet = subnet,
                header = data['header'],
                image = data['image'],
            )
            form.save()
            return HttpResponseRedirect(f'/nets/{net_title}')

@login_required
def post_comment_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    root_post = post.get_root()
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
            return redirect(f"/posts/{root_post.id}/")
    form = CommentForm()
    header = f'Post a comment on \"{post.header}\":'
    return_link = f"/posts/{root_post.id}/"
    context = {'form': form, 'header': header, "root_link":return_link}
    return render(request, "forms.html", context)

@login_required
def upvotes_view(request, post_id):
    current_user = request.user
    post = Post.objects.filter(id=post_id).first()
    if post in current_user.has_liked.all():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        current_user.has_liked.add(post)
        current_user.has_disliked.remove(post)
        post.upvotes +=1
        current_user.save()
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def downvotes_view(request, post_id):
    current_user = request.user
    post = Post.objects.filter(id=post_id).first()
    if post in current_user.has_disliked.all():
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        current_user.has_disliked.add(post)
        current_user.has_liked.remove(post)
        post.downvotes +=1
        current_user.save()
        post.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
