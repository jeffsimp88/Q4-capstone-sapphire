
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, SignupForm
from net_user_app.models import NetUser
# from django.contrib.auth.decorators import login_required
from django.views.generic import FormView, CreateView, View
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class SignupView(CreateView):
    form_class = SignupForm
    success_url = '/'
    template_name = 'forms.html'

    def get(self, req):
        form = SignupForm()
        html = 'forms.html'
        context = {
            'form': form,
            'header': "Signup as a User",
            'signing_in':True
            }
        return render(req, html, context)

    def post(self, req):
        form = SignupForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            if NetUser.objects.filter(username=data['username']).exists():
                messages.warning(
                    req,
                    f"Sorry, username {data['username']} already exists."
                    )
                return redirect('/signup/')
            user = NetUser.objects.create_user(
                username=data['username'],
                email=data['email'],
                password=data['password']
            )
            user = authenticate(
                req,
                username=data['username'],
                password=data['password'])
            if user:
                login(req, user)
                return HttpResponseRedirect(req.GET.get('next', '/'))
        return HttpResponseRedirect(req.GET.get('next', '/'))


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'forms.html'

    def get(self, req):
        form = LoginForm()
        context = {
            'form': form,
            'header': "Login as a User",
            'logging_in': True,
        }
        return render(req, 'forms.html', context)

    def post(self, req):
        form = LoginForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                req,
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(req, user)
                return HttpResponseRedirect(req.GET.get('next', '/'))


class LogoutView(View):
    @method_decorator(login_required)
    def get(self, req):
        logout(req)
        return HttpResponseRedirect('/')
