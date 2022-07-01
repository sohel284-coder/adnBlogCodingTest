from django.urls import path


from blogapp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('create-post/', post_create, name='post_create'), 
]