from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

class PostDetail(DetailView):
    model = Post


# def index(request):
#     posts = Post.objects.all()
#
#     return render(
#         request,
#         'swingpage/post_list.html',
#         {
#             'posts' : posts,
#         }
#     )

# def post_detail(request,pk):
#     detail_post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'swingpage/detail_post.html',
#         {
#             'detail_post' : detail_post
#         }
#     )