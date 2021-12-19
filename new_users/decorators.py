from django.http import HttpResponse
from django.shortcuts import redirect, render


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
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
            # print('customer')

            elif group == 'insuranceCompany':
                return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('Logged Out')

    return wrapper_function
