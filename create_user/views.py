from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def sign_in(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('start_page')

        form = LoginForm()
        return render(request, 'create_user/login.html', {'form': form})

    elif request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Hi {username.title()}, welcome back!')
                return redirect('start_page')

        messages.error(request, f'Invalid username or password')
        return render(request, "create_user/login.html", {"form": form})


def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out')
    return redirect('start_page')


def sign_up(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.username = user.username.lower()
        user.save()
        login(request, user)
        messages.success(request, 'You have signed up successfully.')
        return redirect('start_page')
    else:
        return render(request, 'create_user/register.html', {'form': form})
