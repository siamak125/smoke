from django.shortcuts import render
from post.form import PostForm
from post.models import Post


def Post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = Post(title=form.cleaned_data['title'], body=form.cleaned_data['body'])
            post.save()
            info_post = Post.objects.all()
            body = info_post.body
            print(body)
            form = post
            context = {'form': form}
            return render(request, 'post/post.html', context)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'post/post.html', context)
