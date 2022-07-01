
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from accountapp.forms import CreateNewUserForm



def sign_up(request):
    form = CreateNewUserForm()
    if request.method == 'POST':
        form = CreateNewUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Successfully create account')
            return redirect('login_page')
        else:
            errors = form.errors
            print(errors)
            return render(request, 'account/signup.html', {'form': form, 'errors': errors})               

    return render(request, 'account/signup.html', {
        'title': 'Sign Up User', 'form': form,
    })


def login_page(request):
    context = {}
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password, )
            if user is not None:
                login(request, user)
                messages.success(request, 'Successfully login')
                return redirect('home')
            else:
                context['login_failed'] = True
                print(context)
        else:
            context['login_failed'] = True 
    else:
        context['form'] = form
              

    return render(request, 'account/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login_page') 
