from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm, SignInForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm


# Create your views here.
# def home(request):
#     return render(request, 'base/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('signup')
        
    form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('signup')
    form = SignInForm()
    return render(request, 'auth/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('signup')


def password_change(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('signup')
        form = PasswordChangeForm(request.user)
        return render(request, 'auth/password_change.html', {'form': form})


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(data=request.POST)
        if form.is_valid():
            form.save(
                'Password reset',
                'Password reset mail body here.',

            )
