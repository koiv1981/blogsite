from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag
from django.db.models import F


class Home(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context['title'] = "Главгая страница"
        return context


class PostsByCategory(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = False
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostsByCategory, self).get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])


class PostsByTag(ListView):
    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    allow_empty = True
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostsByTag, self).get_context_data(**kwargs)
        context['title'] = Tag.objects.get(slug=self.kwargs['slug'])
        return context

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])


class GetPost(DetailView):
    model = Post
    template_name = 'blog/single.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GetPost, self).get_context_data(**kwargs)
        context['title'] = Post.objects.get(slug=self.kwargs['slug'])
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Search(ListView):
    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Search, self).get_context_data(**kwargs)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('s'))
