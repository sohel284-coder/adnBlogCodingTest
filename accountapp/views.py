
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from accountapp.forms import CreateNewUserForm
from blogapp.models import Post, Comment



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


def user_list(request, ):
    users = User.objects.all().exclude(is_staff=True)
    return render(request, 'user/user_list.html', {
        'users':users
    })

def user_delete(request, pk):
    user = User.objects.get(pk=pk)
    try:
        posts = Post.objects.filter(author=user)
        for post in posts:
            post.delete()
        print(posts)    
    except Exception as e:
        print(e)
    try:
        commnents = Comment.objects.filter(user=user)
        for comment in commnents:
            comment.delete()
        print(commnents)
    except Exception as e:
        print(e)    
    user.delete()
    messages.info(request, 'successfull user deleted')
    return redirect('user_list')
