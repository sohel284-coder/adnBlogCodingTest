from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


class CreateNewUserForm(UserCreationForm):
    first_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder': 'Enter your first name',
        'class': 'form-control mt-3',  
    }))
    last_name = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder': 'Enter your last name',
        'class': 'form-control mt-3',  
    }))
    email = forms.EmailField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder':'Enter your email address',
        'class': 'form-control mt-3',
    }))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder': 'Enter your username',
        'class': 'form-control mt-3',  
    }))
    password1 = forms.CharField(min_length=8, max_length=32, label="", required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'form-control mt-3',
    }))
    password2 = forms.CharField(min_length=8, max_length=32, label="", required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter password',
        'class': 'form-control mt-3',
    }))
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username','password1', 'password2', )


    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            raise forms.ValidationError("The email is already in use")
        except User.DoesNotExist:
            return email
     

    def clean(self):
        super(CreateNewUserForm, self).clean()
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('repeat_password')
        if not password == re_password:
            raise forms.ValidationError('Password must match')    