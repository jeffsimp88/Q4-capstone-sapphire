from django.shortcuts import render, redirect
from net.models import Net


def subscribe_net(request, net_title, post_id):
    current_user = request.user
    current_net = Net.objects.filter(title=net_title).first()
    current_user.subs.add(current_net)
    current_user.save()
    return redirect(f'/nets/{net_title}/')
    # return redirect('/')
    
