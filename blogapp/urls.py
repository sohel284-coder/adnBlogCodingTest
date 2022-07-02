from unicodedata import name
from django.urls import path


from blogapp.views import *

urlpatterns = [
    path('', all_blogs, name='all_blogs'),
    path('create-post/', post_create, name='post_create'), 
    path('post/<str:slug>/', post_details, name='post_details'),
    path('<int:user>/posts/', user_wise_post_list, name='user_wise_post_list'),
    path('delete-post/<str:slug>/', delete_post, name='delete_post'),
]