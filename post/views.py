from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
        paginator = Paginator(info_post, 5)
        page_num = request.GET.get('page')
        page = paginator.get_page(page_num)
        form = PostForm()
        context = {'form': form,
                   "posts": info_post,
                   'page_obj': page}
        return render(self.request, 'post/post.html', context)
#
#
# class PostCreateListView(ListCreateAPIView):
#     serializer_class = PostSerializer
#     queryset = PostModel
#
#
# class PostRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     serializer_class = PostSerializer
#     queryset = PostModel
#     lookup_field = "id"
