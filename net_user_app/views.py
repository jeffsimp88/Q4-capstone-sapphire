from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from net_user_app.models import NetUser
from net_user_app.forms import NetUserUpdateForm
from posts.models import Post
from net.forms import SearchForm
from direct_messages.forms import DirectMessageForm
from notification.models import Notification
import os

def get_total_user_votes(posts):
    posts = posts
    total_votes = 0
    for post in posts:
        total_votes = total_votes + post.total_score
    return total_votes

def profile_view(request, username):
    context = {}    
    page_user = NetUser.objects.get(username=username)
    followers = page_user.followers.all().order_by("username")
    posts = Post.objects.filter(author=page_user).order_by('-timestamp')
    original_posts = posts.filter(parent=None).order_by('-timestamp')
    subs = page_user.subs.all().order_by('title')
    total_votes = get_total_user_votes(posts)
    if request.user.is_authenticated:
        is_followed = check_follow(request, username)
        message_form = DirectMessageForm()
    else:
        is_followed = ""
    context.update({
        "user": page_user,
        'followers': followers,
        'posts': original_posts,
        'subs': subs,
        'total_votes': total_votes,
        'is_followed': is_followed,
        'message_form': message_form
        })
    return render(request, 'profile.html', context)

def update_user(request, user_id):
    current_user = NetUser.objects.get(id=user_id)
    current_image = current_user.profile_image
    if current_image:
        image_path = current_user.profile_image.path
    else:
        image_path = "dummy string"
    if request.method == "POST":
        form = NetUserUpdateForm(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            if current_image != form.cleaned_data['profile_image']:
                if os.path.exists(image_path):
                    os.remove(image_path)
            form.save()
            messages.success(request, "User info updated successfully.")
            return redirect(f'/users/{current_user.username}/')
    else:
        form = NetUserUpdateForm(initial={'username':current_user.username ,'bio':current_user.bio ,'email':current_user.email , 'profile_image': current_user.profile_image})

    context = {'header': 'Update User Info', 'form': form}
    return render(request, 'forms.html', context)

def change_theme(request):
    current_user = request.user
    if current_user.site_theme == "Light":
        current_user.site_theme = 'Dark'
        current_user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        current_user.site_theme = 'Light'
        current_user.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def check_follow(request, username):
    user_info = NetUser.objects.get(username=username)
    current_user = request.user
    follows = current_user.followers
    if follows.filter(username=username).exists():
        is_followed =True
    else:
        is_followed =False
    return is_followed


def follow_user(request, username):
    current_user = request.user
    other_user = NetUser.objects.get(username=username)
    check_follower = current_user.followers
    is_followed = False
    if check_follower.filter(username=other_user).exists():
        check_follower.remove(other_user)
        is_followed = False
        return redirect(f'/users/{username}/')
    else:
        check_follower.add(other_user)
        Notification.objects.create(
            to_user=other_user,
            created_by=current_user,
            notification_type='Follow'
        )
        is_followed = True
        return redirect(f'/users/{username}/')



def about_us_view(request):
    context={'header': "About us!"}
    return render(request, "about.html", context)
