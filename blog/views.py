from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, PostCategory
from .forms import PostForm
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import CommentForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def article_list_view(request):
    articles = Post.objects.filter(post_type='ARTIGO', status='PUBLISHED')
    context = {
        'posts': articles,
        'page_title': 'Artigos Científicos',
    }
    return render(request, 'blog/post_list.html', context)

def cultivation_tips_view(request):
    categories = PostCategory.objects.all()
    tips_list = Post.objects.filter(post_type='DICA', status='PUBLISHED')
    category_filter_id = request.GET.get('category')
    if category_filter_id:
        tips_list = tips_list.filter(category__id=category_filter_id)
    context = {
        'posts': tips_list,
        'categories': categories,
        'selected_category_id': int(category_filter_id) if category_filter_id else None,
        'page_title': 'Dicas de Cultivo',
    }
    return render(request, 'blog/post_list.html', context)

def post_detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='PUBLISHED')
    comments = post.comments.all()
    comment_form = CommentForm()

    if request.method == 'POST':
        if request.user.is_authenticated:
            comment_form = CommentForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post
                new_comment.author = request.user
                new_comment.save()
                return HttpResponseRedirect(request.path_info)
        else:
            return redirect('users:login')

    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)


class UserPostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/user_post_list.html'
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-published_date')

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:my_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user.role == 'MODERATOR':
            form.instance.status = 'PUBLISHED'
        else:
            form.instance.status = 'PENDING'
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:my_posts')

    def form_valid(self, form):
        form.instance.author = self.request.user
        if self.request.user.role != 'MODERATOR':
            form.instance.status = 'PENDING'
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:my_posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

# moderação

def is_moderator(user):
    return user.is_authenticated and user.role == 'MODERATOR'

class PendingPostsListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Post
    template_name = 'blog/pending_posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def test_func(self):
        return is_moderator(self.request.user)

    def get_queryset(self):
        return Post.objects.filter(status='PENDING').order_by('published_date')

@user_passes_test(is_moderator)
def approve_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.status = 'PUBLISHED'
    post.save()
    return redirect('blog:pending_posts')

@user_passes_test(is_moderator)
def reject_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.status = 'DRAFT'
    post.save()
    return redirect('blog:pending_posts')

@login_required
def like_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog:post_detail', args=[str(pk)]))

@login_required
def save_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    if post.saves.filter(id=request.user.id).exists():
        post.saves.remove(request.user)
    else:
        post.saves.add(request.user)
    return HttpResponseRedirect(reverse('blog:post_detail', args=[str(pk)]))


