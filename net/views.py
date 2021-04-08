from django.shortcuts import render, redirect
from net.forms import CreateNet
from net.models import Net
from net_user_app.models import NetUser
from posts.models import Post
import random

def check_subscribe(request, net_title):
    net_info = Net.objects.get(title=net_title)
    current_user = request.user
    subscribes= current_user.subs
    if subscribes.filter(title=net_title).exists():
        is_subscribed=True
    else:
        is_subscribed=False
    return is_subscribed


def create_net_view(request):
    if request.method == 'POST':
        post = CreateNet(request.POST)
        if post.is_valid():
            data = post.cleaned_data
            new_net = Net.objects.create(
                title=data['title'],
                description=data['description'],
                rules=data['rules'],
                private=data['private'],

                )
            new_net.moderators.add(request.user)
            return redirect("/")
    form = CreateNet()

    context = {'form': form}
    return render(request, 'forms.html', context)



def index_view(request):
    context = {'header': "Welcome to Subnet"}
    posts = Post.objects.all()
    nets = Net.objects.all()
    random_nets = random_net_helper()
    context.update({"posts": posts,
                    "nets": nets,
                    "random": random_nets})
    return render(request, 'homepage.html', context)

def individual_net_view(request, net_title):
    selected_net = Net.objects.filter(title=net_title).first()
    is_subscribed = check_subscribe(request, selected_net)
    user_subs = request.user.subs.all()
    posts = Post.objects.filter(subnet=selected_net)
    context = {
        'net': selected_net,
        'is_subscribed': is_subscribed,
        'posts': posts,
        'subs': user_subs,
        }
    return render(request, 'individual_nets.html', context)

def subscribe_net(request, net_title):
    current_user = request.user
    current_net = Net.objects.get(title=net_title)
    check_sub = current_user.subs
    is_subscribed = False
    if check_sub.filter(title=current_net).exists():
        check_sub.remove(current_net)
        is_subscribed = False
        return redirect(f'/nets/{net_title}/')
    else:
        check_sub.add(current_net)
        is_subscribed = True
        return redirect(f'/nets/{net_title}/')


def random_net_helper():
    nets = Net.objects.all()
    random_nets = []
    random_index_list = []
    for num in range(50): 
        if len(random_index_list) < 10:  
            random_num = random.randrange(1, len(nets))
            if random_num not in random_index_list:
                random_index_list.append(random_num)
    for each in random_index_list:
        random_nets.append(nets[each])
    return random_nets




