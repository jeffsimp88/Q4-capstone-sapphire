from django.shortcuts import render, redirect, HttpResponseRedirect
from net_user_app.models import NetUser
from posts.models import Post

def get_total_user_votes(posts):
    posts = posts
    total_upvotes = 0
    total_downvotes = 0
    for post in posts:
        total_upvotes = total_downvotes + post.upvotes
        total_downvotes = total_downvotes + post.downvotes
    return (total_upvotes - total_downvotes)

def profile_view(request, username):
    context = {}
    page_user = NetUser.objects.get(username=username)
    followers = page_user.followers.all().order_by("username")
    posts = Post.objects.filter(author=page_user).order_by('timestamp')
    total_votes = get_total_user_votes(posts)
    is_followed = check_follow(request, username)
    context.update({
        "user": page_user,
        'followers': followers,
        'posts': posts, 
        'total_votes': total_votes,
        'is_followed': is_followed,
        })
    return render(request, 'profile.html', context)

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
        is_followed = True
        return redirect(f'/users/{username}/')


