from django.http import HttpResponse
from django.shortcuts import redirect, render

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

            if group == 'FieldAgent':
                return render(request, 'fa_dash.html')
            #print('customer')

            elif group == 'insuranceCompany':
                return view_func(request, *args, **kwargs)
        else:
            return HttpResponse('You are not assigned to any group yet')

    return wrapper_function