from django.shortcuts import render, redirect
from django.contrib import messages
from net.forms import CreateNet, SearchForm, UserSearchForm, ChangeModerators, ChangeSubscribers
from net.models import Net
from net_user_app.models import NetUser
from posts.models import Post


def index_view(request):
    net_not_found = False
    user_not_found = False
    context = {}
    if request.user.is_authenticated:
        followers = request.user.followers.all().order_by("username")
        sub_nets = request.user.subs.all().order_by('title')
        posts = []
        for sub in sub_nets:
            posts += Post.objects.filter(subnet=sub).order_by('-timestamp')
        posts.sort(key=lambda x:x.timestamp, reverse=True)
    else:
        followers = []
        sub_nets = []
        posts = recent_posts_helper()

    if request.method == 'POST':
        return_url = search_net(request)
        searched_user_url = search_user(request)
        if return_url:
            return redirect(return_url)
        if searched_user_url: 
            return redirect(searched_user_url)
        elif not return_url and searched_user_url == None:
            messages.error(request, "Not found. Please Try Again!")
            net_not_found = True
        elif not searched_user_url and return_url == None:
            messages.error(request, "User not Found. Please Try Again!")
            user_not_found = True
    nets = Net.objects.all().order_by('title')
    search_form = SearchForm()
    user_search = UserSearchForm()
    context.update({
        "sub_nets": sub_nets,
        'followers': followers,
        "nets": nets,
        "posts": posts,
        "search_form": search_form,
        "user_form": user_search,
        "net_not_found": net_not_found,
        "user_not_found": user_not_found,
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
            if items.title.casefold() == data["search_info"].casefold():       
                return (f"/nets/{items.title}/")         


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
    if request.user.is_authenticated:
        is_subscribed = check_subscribe(request, selected_net)
    else:
        is_subscribed=""
    search_form = SearchForm()
    user_form = UserSearchForm()
    posts = Post.objects.filter(subnet=selected_net).order_by("-timestamp")
    moderators = selected_net.moderators.all().order_by('username')
    subscribers = NetUser.objects.filter(subs__title=selected_net.title)
    if request.user not in subscribers and selected_net.private:
        print("NOT WORTHY!")
        allow_user = False
    else:
        print("They may enter")
        allow_user = True
    context = {
        'net': selected_net,
        'moderators': moderators,
        'subscribers': subscribers,
        'is_subscribed': is_subscribed,
        'user_allowed': allow_user,
        'posts': posts,
        'search_form': search_form,
        'user_form': user_form,
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

def change_moderators(request, net_title):
    current_net = Net.objects.get(title=net_title)
    current_moderators = current_net.moderators.all().order_by('username')
    current_subscribers = NetUser.objects.filter(subs__title=current_net.title) 
    if request.method == 'POST':
        form = ChangeModerators(request.POST)
        if form.is_valid():
            current_net.moderators.set(form.cleaned_data['moderators'])
            return redirect(f'/nets/{net_title}/')
    form = ChangeModerators(initial={'moderators': current_moderators})
    form.fields['moderators'].queryset = current_subscribers.order_by('username')
    context = {'form': form}
    return render(request, "forms.html", context)

def change_subscribers(request, net_title):
    current_net = Net.objects.get(title=net_title)
    current_moderators = current_net.moderators.all().order_by('username')
    users = NetUser.objects.all()
    current_subscribers = NetUser.objects.filter(subs__title=current_net.title)
    if request.method == 'POST':
        form = ChangeSubscribers(request.POST)
        if form.is_valid():
            selected_users = form.cleaned_data['subscribers']
            for user in selected_users:
                user.subs.add(current_net)
            return redirect(f'/nets/{net_title}/')
    form = ChangeSubscribers(initial={'subscribers': current_subscribers})
    context = {'form': form}
    return render(request, "forms.html", context)

def recent_posts_helper():
    posts = Post.objects.filter(post_type='Post')
    recent_posts = list(posts.order_by('-timestamp')[0:10])
    return recent_posts


def error_404_view(request, exception):
    return render(request,'404.html')


def search_user(request):
    search = UserSearchForm(request.POST)
    if search.is_valid():
        data = (search.cleaned_data)
        for users in NetUser.objects.all():
            if users.username.casefold() == data['user_info'].casefold():
                return(f"/users/{users.username}/")





