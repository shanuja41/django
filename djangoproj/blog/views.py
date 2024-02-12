from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# def home(request):
#     context = {
#         'posts': post.objects.all()
#     }
#     return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html', {'title':'About Page '})

class PostListView(LoginRequiredMixin,  ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(LoginRequiredMixin , DetailView):
    model = post

class PostCreateView(LoginRequiredMixin ,  CreateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def test_func(self):
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False
class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin, UpdateView):
    model = post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(DeleteView):
    model = post
    success_url ='/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False




