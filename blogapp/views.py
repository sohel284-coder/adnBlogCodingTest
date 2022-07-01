from django.shortcuts import render


def home(request, ):
    return render(request, 'home.html')



def post_create(request, ):
    return render(request, 'blog/create_post.html', )