from tokenize import Comment
from django.contrib import admin

from blogapp.models import Post, Comment


admin.site.register(Post)
admin.site.register(Comment)