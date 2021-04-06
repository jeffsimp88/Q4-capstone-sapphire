from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, SignupForm
from django.contrib.auth.decorators import login_required


def signup_view(request):
    # if request.method == 'POST':
    #     form = SignupForm(request.POST)
    #     if form.is_valid():
    #         data = form.cleaned_data
    #         new_user = CustomUser.objects.create_user(
    #             username=data['username'],
    #             email = data['email'],
    #             password=data['password']
    #         )
    #         user = authenticate(
    #             request, username=data['username'], password=data['password']
    #         )
    #         if user:
    #             login(request, user)
    #             return HttpResponseRedirect(request.GET.get('next', '/'))
            
    form = SignupForm()
    context ={
        'form': form,
        'heading': "Signup as a User",
        'signing_in': True,
    }
    return render(request, "forms.html", context)


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', '/'))
    form = LoginForm()
    context = {
        'form': form,
        'heading': "Login as a User",
        'logging_in': True,
    }
    return render(request, 'forms.html', context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
