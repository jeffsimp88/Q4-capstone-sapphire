from django.shortcuts import render, redirect, HttpResponseRedirect
from posts.forms import PostForm, CommentForm, PostImage
from posts.models import Post
from net.models import Net
from notification.utilities import create_notification


def individual_post_view(request, post_id):
    context = {'header': "Post Details"}
    post = Post.objects.get(id=post_id)
    comments = Post.objects.filter(parent=post)
    context.update({'post': post, 'comments': comments})
    return render(request, 'individual_posts.html', context)

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
    form = PostForm()
    context.update({'form':form})
    return render(request, 'forms.html', context)

def post_image_view(request, net_title):
    context = {'header': "Post a Post"}
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
    form = PostImage()
    context.update({'form':form})
    return render(request, 'forms.html', context)


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
            create_notification(request, post.created_by, 'new_post', extra_id=new_post.id)
            return redirect(f"/posts/{root_post.id}/")
    form = CommentForm()
    context = {'form': form}
    return render(request, "forms.html", context)

def upvotes_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    post.upvotes +=1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvotes_view(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    post.downvotes +=1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
