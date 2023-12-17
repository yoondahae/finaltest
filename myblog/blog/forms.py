# forms.py

from django import forms
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Post
from .models import Comment
class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'author', 'image')

class SignupForm(forms.ModelForm):
    # 회원가입 폼 정의
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']