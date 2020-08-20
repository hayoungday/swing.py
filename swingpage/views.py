from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



# Create your views here.

class PostList(ListView):
    model = Post
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Post.objects.order_by('-created')

class PostDetail(DetailView):
    model = Post
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context

class PostUpdate(UpdateView):
    model = Post
    fields = [
        'title', 'content', 'head_image'
    ]
    # def form_valid(self, form):
    #     form.save(commit=True)
    #     return super(PostUpdate, self).form_valid(form)
    # def get_context_data(self, **kwargs):
    #     context = super(PostUpdate, self).get_context_data(**kwargs)
    #     context['action'] = reverse('post-edit', kwargs={'pk':self.get_object().id})
    #     return context


class PostCreate(CreateView):
    model = Post
    fields = [
        'title', 'content', 'head_image'
    ]
    def form_valid(self, form):
        current_user = self.request.user

        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(type(self), self).form_valid(form)
        else:
            return redirect('/swingpage/')

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('homepage')

    def get_object(self, queryset=None):
        post = super(PostDelete, self).get_object()
        if post.author != self.request.user:
            raise PermissionError('no permission')
        return post
