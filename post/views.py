from django.shortcuts import render
from post.form import PostForm


def Post(request):
    form = PostForm()
    context = {'form': form}
    return render(request, 'post/post.html', context)
