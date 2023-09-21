from typing import Any, Dict
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.views.generic.base import TemplateView
from django.views import View
from .forms import PostForm


def allblogs(request):
    return render(request, 'blog/allblogs.html', )

def about(request):
    return render(request, 'blog/about.html', )

def firstpage(request):
    return render(request, 'blog/firstpage.html', )

def accessDenied(request):
    return render(request, 'blog/404.html', )

class AllBlogsView(View):
    template_name = 'blog/allblogs.html'
    redirect_url = 'access-denied'

    def get(self, request):
        if request.user.is_authenticated and request.user.is_staff:
            posts = Post.objects.order_by('date_posted')  # Fetch all blogs
            return render(request, self.template_name, {'posts': posts})
        else:
            return redirect(self.redirect_url)

    
class PostCreateView(View):
    template_name = 'blog/new_post.html'
    
    def get(self, request):
        if self.request.user.is_superuser:
            form = PostForm()
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('login')

    def post(self, request):
        form = PostForm(request.POST)
        print(request.user)

        if form.is_valid():
            if self.request.user.is_superuser:
                form.instance.author = self.request.user
                new_post = form.save()
                return redirect('blog-detail', blog_id= new_post.id)
            else:
                return redirect('login')
        return render(request, self.template_name, {'form': form})


class PostDetailView(View):
    template_name = 'blog/post_detail.html'
    def get(self, request, blog_id):
        print(blog_id)
        blog = get_object_or_404(Post, id=blog_id)
        print(blog.author)
       
        return render(request, self.template_name, {'blog':blog})
    
class PostUpdateView(View):
    template_name = 'blog/post_update.html'
    
    def get(self, request, blog_id):
        blog = get_object_or_404(Post, id=blog_id)
        form = PostForm(instance = blog)
        return render(request, self.template_name, {'form': form, 'blog':blog})
    
    def post(self, request, blog_id):
        blog = get_object_or_404(Post, id=blog_id)
        form = PostForm(request.POST, instance = blog)

        if form.is_valid():
            form.save()
            return redirect('blog-detail', blog_id=blog.id)
        
        return render(request, self.template_name, {'form': form, 'blog':blog})
    
class PostDeleteView(View):
    template_name = 'blog/post_delete.html'

    def get(self, request, blog_id):
        blog = get_object_or_404(Post, id=blog_id)
        return render(request, self.template_name, {'blog':blog})
    
    def post(self, request, blog_id):
        blog = get_object_or_404(Post, id=blog_id)
        blog.delete()

        return redirect('all-blogs')
    

        
