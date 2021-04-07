from django.shortcuts import render, redirect
from net.forms import Create_Net
from net.models import Net
from net_user_app.models import NetUser
from posts.models import Post


def check_subscribe(request, net_title):
    net_info = Net.objects.get(title=net_title)
    current_user = request.user
    subscribes= current_user.subs
    if subscribes.filter(title=net_title).exists():
        is_subscribed=True
    else:
        is_subscribed=False
    return is_subscribed


def net_main_view(request):
    if request.method == 'POST':
        post = Create_Net(request.POST)
        if post.is_valid():
            data = post.cleaned_data
            Net.objects.create(
                title=data['title'],
                description=data['description']
                )
            return redirect("/")
    form = Create_Net()

    context = {'form': form}
    return render(request, 'newnet.html', context)



def index_view(request):
    context = {'header': "Welcome to Subnet"}
    posts = Post.objects.all()
    nets = Net.objects.all()
    context.update({"posts": posts,
                    "nets": nets})
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
        print("You are now unsubscribed")
        check_sub.remove(current_net)
        is_subscribed = False
        return redirect(f'/nets/{net_title}/')
    else:
        check_sub.add(current_net)
        is_subscribed = True
        return redirect(f'/nets/{net_title}/')

