from django.shortcuts import render, redirect
from net.forms import Create_Net

def net_main_view(request):
    if request.method = 'POST':
        post = Create_Net(request.POST)
        if post.is_valid():
            clean = post.cleaned_data
            if clean['post_type'] = "Net":
                post.objects.create(
                    author=request.user
                    header=clean['title']
                    content=clean['content']
                )
            return redirect("/")
    form = Create_Net
    return render(request, 'newNet.html', {form:'form'})


