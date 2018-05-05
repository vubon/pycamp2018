from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm

from .forms import SignUpForm, SignInForm

def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
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
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    form = SignInForm()
    return render(request, 'auth/signin.html', {'form': form})


def signout(request):
    logout(request)
    return redirect('home')


def password_change(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, data=request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        form = PasswordChangeForm(request.user)
        return render(request, 'auth/password_change.html', {'form': form})


def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                from_email='from@example.com',
                email_template_name='registration/password_reset_body.html'
            )
            return redirect('home')
    form = PasswordResetForm(None)
    return render(request, 'auth/password_reset.html', {'form': form})
