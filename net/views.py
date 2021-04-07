from django.shortcuts import render
from net.models import Net
from posts.models import Post

# Create your views here.
def index_view(request):
    context = {'header': "Welcome to Subnet"}
    posts = Post.objects.all()
    context.update({"posts": posts})
    return render(request, 'homepage.html', context)
