from django import forms
from post.models import Post


class PostForm(forms.Form):
    title = forms.CharField(max_length=200)
    body = forms.CharField(max_length=900)
