
import uuid

from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from blogapp.models import Post
from blogapp.froms import PostForm, CommentForm
from django.contrib import messages



def home(request, ):
    posts = Post.objects.all().order_by('-publish_date')
    return render(request, 'home.html', {
        'posts':posts, 
    })


def post_create(request, ):
    form = PostForm()
    context = {}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post_obj = form.save(commit=False)
            post_obj.author = request.user
            title = post_obj.title
            post_obj.slug = title.replace(' ', '_') + '_' + str(uuid.uuid4())
            print(request.FILES)
            post_obj.image = request.FILES['image']
            post_obj.save()
            messages.success(request, 'Post is successfully created')
            return redirect('post_create')
        else:
            context['create_failed'] = True
    else:
        context['form'] = form

    return render(request, 'blog/create_post.html', context)



def post_details(request, slug):
    post = Post.objects.get(slug=slug)
   
    
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet          
            comment_obj = comment_form.save(commit=False)
            # Assign the current post to the comment
            comment_obj.post = post
            # Assign the current user to the comment
            comment_obj.user = request.user
            # Save the comment to the database
            comment_obj.save()
            messages.success(request, 'Successfully comment on post !')
            return redirect('post_details', slug=slug)
    else:
        comment_form = CommentForm() 
    return render(request, 'blog/post_details.html', {
        'post':post, 
        'comment_form':comment_form,
    })


def user_wise_post_list(request, user):
    user = User.objects.get(pk=user)
    posts = Post.objects.filter(author=user)
    return render(request, 'blog/user_wise_post_list.html', {
        'posts':posts,
    })

def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    post.delete()
    return redirect('user_wise_post_list',  user=request.user.pk)