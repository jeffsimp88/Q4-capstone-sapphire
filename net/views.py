from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'index.html', {'posts': posts})

def error_404_view(request, exception):
    return render(request,'404.html')