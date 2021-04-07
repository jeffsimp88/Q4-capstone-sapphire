from django.shortcuts import render, redirect
from net.forms import Create_Net
from net.models import Net
from posts.models import Post

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
    user_subs = request.user.subs.all()
    context = {'net': selected_net, 'subs': user_subs}
    return render(request, 'individual_nets.html', context)
