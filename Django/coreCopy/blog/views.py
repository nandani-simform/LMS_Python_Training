from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic.base import TemplateView
from django.views import View
from .forms import PostForm
from django.http import HttpResponseRedirect


def allblogs(request):
    return render(request, 'blog/allblogs.html', )

def about(request):
    return render(request, 'blog/about.html', )

def firstpage(request):
    return render(request, 'blog/firstpage.html', )

class AllBlogsView(TemplateView):
    template_name = 'blog/allblogs.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context
    
class PostCreateView(View):
    template_name = 'blog/new_post.html'
    
    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        print(request.user)

        if form.is_valid():
            form.instance.author = self.request.user
            new_post = form.save()
            return redirect('blog-detail', pk = new_post.pk)
        return render(request, self.template_name, {'form': form})

class PostDetailView(View):
    def get(self, request, pk):
        form = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'form': form})
    
