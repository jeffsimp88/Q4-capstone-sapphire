from django.shortcuts import render, redirect
from net_user_app.models import NetUser

def profile_view(request, username):
    context = {}
    page_user = NetUser.objects.get(username=username)
    print(page_user)
    context.update({"user": page_user})
    return render(request, 'profile.html', context)

    
