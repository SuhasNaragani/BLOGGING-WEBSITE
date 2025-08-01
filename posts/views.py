# posts/views.py

from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from datetime import datetime

from .models import Post
from .forms import CommentForm
from .serializers import PostSerializer
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = Post.objects.filter(status='published').order_by('-created_at')
        
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(body__icontains=query)
            )
            
        search_date = self.request.GET.get('date')
        if search_date:
            try:
                selected_date = datetime.strptime(search_date, '%Y-%m-%d').date()
                queryset = queryset.filter(created_at__date=selected_date)
            except (ValueError, TypeError):
                pass
                
        return queryset


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.author = request.user
            comment.save()
            return redirect('post_detail', slug=self.object.slug)
        else:
            context = self.get_context_data()
            context['comment_form'] = form
            return self.render_to_response(context)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body', 'status', 'image'] # ADD 'image'
    template_name = 'posts/post_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'body', 'status', 'image'] # ADD 'image'
    template_name = 'posts/post_form.html'
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class DashboardView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'posts/dashboard.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user).order_by('-created_at')


class PostApiViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A read-only API endpoint for viewing posts.
    """
    queryset = Post.objects.filter(status='published')
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = UserUpdateForm(instance=request.user)
    
    return render(request, 'registration/profile_edit.html', {'form': form})


# posts/views.py
# ... (keep all your existing code) ...

# ADD THIS NEW FUNCTION
def support_page(request):
    context = {
        'title': 'Support & Contact'
    }
    return render(request, 'posts/support.html', context)