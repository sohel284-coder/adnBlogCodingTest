
from django import forms

from blogapp.models import Post, Comment


class PostForm(forms.ModelForm):

    title = forms.CharField(required=True, label="Title", widget=forms.TextInput(attrs={
        'placeholder': 'Enter title',
        'class': 'form-control mb-3 shadow-sm border-primary',  
    }))
    description = forms.CharField(required=True, label="Description", widget=forms.Textarea(attrs={
        'placeholder': 'Enter description',
        'class': 'form-control mb-3 shadow-sm border-primary',
        'rows':5
        
    }))
    image = forms.FileField(required=True, widget=forms.FileInput(attrs={
        "class":'border-primary shadow-sm'
    }))

    class Meta:
        model = Post
        fields = ('title', 'description',  'image', )


class CommentForm(forms.ModelForm):
    body = forms.CharField(required=True, label="", widget=forms.Textarea(attrs={
        'placeholder': '',
        'class': 'form-control shadow-sm',
        'rows':4
        
    }))

    class Meta:
        model = Comment
        fields = ('body', )


        



