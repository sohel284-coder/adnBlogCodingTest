
from django.db import models
from django.contrib.auth.models import User



class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author', )
    title = models.CharField(max_length=255, )
    description = models.TextField()
    image = models.ImageField(upload_to='blog_img', )
    slug = models.SlugField(max_length=500, unique=True, )
    publish_date = models.DateTimeField(auto_now_add=True, )
    update_date = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment', )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment', )
    body = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ('-comment_date', )
       
    def __str__(self):
        return 'Comment by {} on {}'.format(self.user.username, self.post.title) 
