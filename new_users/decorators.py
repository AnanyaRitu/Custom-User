from django.http import HttpResponse
from django.shortcuts import redirect, render


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('ic_dash')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

            if group == 'FieldAgent':
                return redirect('fa_dash')
            #print('customer')

            elif group == 'insuranceCompany':
                return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not assigned to any group yet')

    return wrapper_function

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print(group)
                #return view_func(request, *args, **kwargs)

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('you are not authorized to view this page')
        return wrapper_func
    return decorator