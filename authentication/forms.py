from django import forms

class SignupForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)