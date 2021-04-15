from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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
            found = Post.objects.filter(subnet=sub)
            posts += found.filter(post_type='Post')
        posts.sort(key=lambda x:x.timestamp, reverse=True)
    else:
        followers = []
        sub_nets = []
        posts = recent_posts_helper()
        popular_nets = most_popular_nets_helper()
    nets = Net.objects.all().order_by('title')
    newest_nets = Net.objects.all().order_by('-creation_date')[:10]
    popular_nets = Net.objects.all().order_by('-subscribers')[:10]
    context.update({
        "sub_nets": sub_nets,
        'followers': followers,
        "popular_nets": popular_nets,
        "posts": posts,
        "newest_nets": newest_nets
        })
    return render(request, 'homepage.html', context)

""" Search Functionality """

def search_request_view(request):
    if request.method == 'POST':
        return_url = search_net(request)
        searched_user_url = search_user(request)
        if return_url:
            return redirect(return_url)
        if searched_user_url: 
            return redirect(searched_user_url)
        else:
            messages.error(request, "Sorry, not found")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def search_net(request):
    search = SearchForm(request.POST)
    if search.is_valid():
        data = (search.cleaned_data)
        for items in Net.objects.all():
            if items.title.casefold() == data["search_info"].casefold():       
                return (f"/nets/{items.title}/")  

def search_user(request):
    search = UserSearchForm(request.POST)
    if search.is_valid():
        data = (search.cleaned_data)
        for users in NetUser.objects.all():
            if users.username.casefold() == data['user_info'].casefold():
                return(f"/users/{users.username}/")

""" Search Functionality END """

""" Helper Functions """

def most_popular_nets_helper(request):
    return Net.objects.all().order_by('-subscribers')[:10]

def recent_posts_helper():
    posts = Post.objects.filter(post_type='Post')
    recent_posts = list(posts.order_by('-timestamp')[0:10])
    return recent_posts  

""" Helper Functions END """

def check_subscribe(request, net_title):
    net_info = Net.objects.get(title=net_title)
    current_user = request.user
    subscribes = current_user.subs
    if subscribes.filter(title=net_title).exists():
        is_subscribed =True
    else:
        is_subscribed =False
    return is_subscribed


       


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

    posts = Post.objects.filter(subnet=selected_net).order_by("-timestamp")
    moderators = selected_net.moderators.all().order_by('username')
    subscribers = NetUser.objects.filter(subs__title=selected_net.title)
    if request.user not in subscribers and selected_net.private:
        allow_user = False
    else:
        allow_user = True
    context = {
        'net': selected_net,
        'moderators': moderators,
        'subscribers': subscribers,
        'is_subscribed': is_subscribed,
        'user_allowed': allow_user,
        'posts': posts,
        }
    return render(request, 'individual_nets.html', context)


def subscribe_net(request, net_title):
    current_user = request.user
    current_net = Net.objects.get(title=net_title)
    print('current_net',current_net)
    check_sub = current_user.subs
    print('check_sub:', check_sub)
    is_subscribed = False
    if check_sub.filter(title=current_net).exists():
        check_sub.remove(current_net)
        current_net.subscribers -= 1
        current_net.save()
        print("sub_count",current_net.subscribers)
        if current_user in current_net.moderators.all():
            current_net.moderators.remove(current_user)
        is_subscribed = False
        return redirect(f'/nets/{net_title}/')
    else:
        check_sub.add(current_net)
        current_net.subscribers += 1
        current_net.save()
        print("sub_count",current_net.subscribers)
        is_subscribed = True
        return redirect(f'/nets/{net_title}/')

@login_required
def change_moderators(request, net_title):
    current_net = Net.objects.get(title=net_title)
    current_moderators = current_net.moderators.all().order_by('username')
    current_subscribers = NetUser.objects.filter(subs__title=current_net.title) 
    if request.method == 'POST':
        form = ChangeModerators(request.POST)
        if form.is_valid():
            current_net.moderators.set(form.cleaned_data['moderators'])
            return redirect(f'/nets/{net_title}/')
    if request.user not in current_moderators:
        form=None
    else:
        form = ChangeModerators(initial={'moderators': current_moderators})
        form.fields['moderators'].queryset = current_subscribers.order_by('username')
    context = {'form': form}
    return render(request, "forms.html", context)

@login_required
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
    if request.user not in current_moderators:
        form=None
    else:
        form = ChangeSubscribers(initial={'subscribers': current_subscribers})
    context = {'form': form}
    return render(request, "forms.html", context)




def error_404_view(request, exception):
    return render(request,'404.html')








