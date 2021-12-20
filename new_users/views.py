from django.http.request import validate_host
from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .forms import Log_in_form,CreateUserForm
from django.contrib.auth.models import Group
from django.contrib import messages
from .decorators import admin_only, unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
import requests


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


@login_required(login_url='login')
def log_out(request):
    logout(request)
    return redirect('login')


#@login_required(login_url='login')
#@allowed_users(allowed_roles=['insuranceCompany'])
def registration(request):
    username=val()
    req=requests.get("https://secret-gorge-75679.herokuapp.com/user/"+username)
    if req.json():
        email=req.json()[0]['email']
        username=req.json()[0]['username']
        form = CreateUserForm(initial={'user_name': username, 'email':email})

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
                messages.info(request, 'Something went wrong')

        context = {'form': form, 'username':username, "email":email}
    
        return render(request,'registration.html', context)
    else:
        return HttpResponse("Please enter username correctly")



@login_required(login_url='login')
@allowed_users(allowed_roles=['FieldAgent'])
def FA_dash(request):
    return render(request, 'fa_dash.html')



@login_required(login_url='login')
@admin_only
def IC_dash(request):
    return render(request, 'ic_dash.html')

def user_name_input(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        print(username)
        global val
        def val():
            return username
        return redirect('registration')
    return render(request, 'user_name.html')