from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import Log_in_form, CreateUserForm
from django.contrib.auth.models import Group
from django.contrib import messages
from .decorators import admin_only, unauthenticated_user

# Create your views here.


@unauthenticated_user
def Login(request):
    form = Log_in_form()

    if request.method == 'POST':
        #form = Log_in_form(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('logged in')
            login(request, user)
            return redirect('ic_dash')
    context = {'form': form}
    return render(request, 'login.html', context)


def log_out(request):
    logout(request)
    return redirect('login')


def registration(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('user_name')
            group = Group.objects.get(name='FieldAgent')
            user.groups.add(group)
            messages.success(
                request, 'Account was created for ' + username)
            return redirect('login')
        else:
            messages.info(request, 'Username Or password incorrect')
    context = {'form': form}
    return render(request, 'registration.html', context)


def FA_dash(request):
    return render(request, 'fa_dash.html')


@admin_only
def IC_dash(request):
    return render(request, 'ic_dash.html')
