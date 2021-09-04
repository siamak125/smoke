from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework.views import APIView

from post.form import PostForm
from post.models import PostModel


# from post.serializers import PostSerializer


class PostAPIView(APIView):

    def post(self, request):
        form = PostForm(self.request.POST)
        if form.is_valid():
            post = PostModel(title=form.cleaned_data['title'],
                             body=form.cleaned_data['body'])
            post.save()
            info_post = PostModel.objects.all()
            paginator = Paginator(info_post, 5)
            print(info_post.count())
            page_num = request.GET.get('page')
            page = paginator.get_page(page_num)

            context = {'form': form,
                       'page_obj': page}
            return render(self.request, 'post/post.html', context)

    def get(self, request):
        info_post = PostModel.objects.all()
        print(info_post.count())
        paginator = Paginator(info_post, 6)
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)
        form = PostForm()
        context = {'form': form,
                   "posts": info_post,
                   'page_obj': page}
        return render(self.request, 'post/post.html', context)


def like(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = PostModel.objects.get(id=post_id)

        if user in post_obj.likes.all():
            post_obj.likes.remove(user)
        else:
            post_obj.likes.add(user)
        data = {
            "likes_count": post_obj.likes.count(),
            "id": post_id
        }
        print(data)
        return JsonResponse(data)

# class PostCreateListView(ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = PostModel
#
#
# class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = PostModel
#     lookup_field = "id"
