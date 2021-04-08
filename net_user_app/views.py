from django.shortcuts import render, redirect, HttpResponseRedirect
from net_user_app.models import NetUser

def profile_view(request, username):
    context = {}
    is_followed = check_follow(request, username)
    page_user = NetUser.objects.get(username=username)
    context.update({"user": page_user, 'is_followed': is_followed})
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


