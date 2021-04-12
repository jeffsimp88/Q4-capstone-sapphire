from django.shortcuts import render, redirect
from django.contrib import messages
from net.forms import CreateNet, SearchForm
from net.models import Net
from net_user_app.models import NetUser
from posts.models import Post
import random


def index_view(request):
    not_found = False
    if request.method == 'POST':
        return_url = search_net(request)
        if return_url:
            return redirect(return_url)
        else:
            messages.error(request, "Net not found. Please Try Again!")
    context = {'header': "Welcome to Subnet"}
    posts = Post.objects.all()
    nets = Net.objects.all().order_by('title')
    sub_nets = filter_sub(request)
    recent_posts = recent_posts_helper()
    search_form = SearchForm()
    context.update({
        "posts": posts,
        "sub_nets": sub_nets,
        "nets": nets,
        "recent_posts": recent_posts,
        "search_form": search_form,
        })
    return render(request, 'homepage.html', context)


def check_subscribe(request, net_title):
    net_info = Net.objects.get(title=net_title)
    current_user = request.user
    subscribes = current_user.subs
    if subscribes.filter(title=net_title).exists():
        is_subscribed =True
    else:
        is_subscribed =False
    return is_subscribed


def search_net(request):
    search = SearchForm(request.POST)
    if search.is_valid():
        data = (search.cleaned_data)
        for items in Net.objects.all():
            if items.title == data["search_info"]:       
                return (f"/nets/{data['search_info']}/")         


def create_net_view(request):
    if request.method == 'POST':
        post = CreateNet(request.POST)
        if post.is_valid():
            data = post.cleaned_data
            if Net.objects.filter(title=data['title']).exists():
                messages.warning(request, f"Sorry, net {data['title']} already exists.")
                return redirect('/newnet/')
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




def individual_net_view(request, net_title):
    selected_net = Net.objects.filter(title=net_title).first()
    is_subscribed = check_subscribe(request, selected_net)
    user_subs = request.user.subs.all()
    posts = Post.objects.filter(subnet=selected_net).order_by("-timestamp")
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


def recent_posts_helper():
    posts = Post.objects.filter(post_type='Post')
    recent_posts = list(posts.order_by('-timestamp')[0:10])
    return recent_posts


def error_404_view(request, exception):
    return render(request,'404.html')

def filter_sub(request):
    net_list = Net.objects.all()
    sub_list = request.user.subs.all()
    new_list = []
    for sub in sub_list:
        if sub in sub_list:
            new_list.append(sub)
    return new_list


