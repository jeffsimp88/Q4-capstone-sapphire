from django.shortcuts import render, HttpResponseRedirect
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
            'heading': "Signup as a User",
            'signing_in': True,
            }
        return render(req, html, context)

    def post(self, req):
        form = SignupForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = NetUser.objects.create_user(
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


# def signup_view(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_user = NetUser.objects.create_user(
#                 username=data['username'],
#                 email = data['email'],
#                 password=data['password']
#             )
#             user = authenticate(
#                 request, username=data['username'], password=data['password']
#             )
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(request.GET.get('next', '/'))
#     form = SignupForm()
#     context ={
#         'form': form,
#         'heading': "Signup as a User",
#         'signing_in': True,
#     }
#     return render(request, "forms.html", context)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'forms.html'

    def get(self, req):
        form = LoginForm()
        context = {
            'form': form,
            'heading': "Login as a User",
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


# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(
#                 request,
#                 username=data['username'],
#                 password=data['password'],
#             )
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(request.GET.get('next', '/'))
#     form = LoginForm()
#     context = {
#         'form': form,
#         'heading': "Login as a User",
#         'logging_in': True,
#     }
#     return render(request, 'forms.html', context)

class LogoutView(View):
    @method_decorator(login_required)
    def get(self, req):
        logout(req)
        return HttpResponseRedirect('/')


# def logout_view(request):
#     logout(request)
#     return HttpResponseRedirect('/')
