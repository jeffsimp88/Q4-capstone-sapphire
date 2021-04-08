from django.shortcuts import render, redirect, HttpResponseRedirect
from net_user_app.models import NetUser

def profile_view(request, username):
    context = {}
    page_user = NetUser.objects.get(username=username)
    context.update({"user": page_user})
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

