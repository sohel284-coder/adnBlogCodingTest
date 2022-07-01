
from django.urls import path

from accountapp.views import *


urlpatterns = [
    path('signup/', sign_up, name='sign_up'),
    path('login/', login_page, name='login_page'), 
    path('logout/', logout_user, name='logout_user'),

]