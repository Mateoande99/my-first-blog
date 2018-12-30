from django.shortcuts import render , get_object_or_404
from apps.blog.models import Post, Blog
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy

class BlogList(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    success_url = reverse_lazy('blog:post_list')


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('pk')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail',pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
