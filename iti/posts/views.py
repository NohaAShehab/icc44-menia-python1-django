from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from posts.forms import PostModelForm
# Create your views here.
from posts.models import Post


class PostCreateView(CreateView):
    template_name = 'posts/create.html'
    form_class =  PostModelForm
    success_url =reverse_lazy('posts.index')


class PostListView(ListView):
    model = Post
    template_name = 'posts/index.html'
    # context_object_name = "posts"
    # queryset = Post.get_all_objects()




class PostEditView(UpdateView):
    template_name = 'posts/edit.html'
    form_class =  PostModelForm
    success_url =reverse_lazy('posts.index')
    # queryset = Post.get_all_objects()
    model = Post


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/show.html'



class PostDeleteView(DeleteView):
    # template_name = 'posts/delete.html'
    success_url =reverse_lazy('posts.index')
    model = Post
