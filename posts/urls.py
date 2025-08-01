# posts/urls.py

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    signup,
    DashboardView,
    profile_edit,
    support_page
)

urlpatterns = [
    # Main pages
    path('', PostListView.as_view(), name='post_list'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    # Auth pages
    path('signup/', signup, name='signup'),
    path('profile/edit/', profile_edit, name='profile_edit'),
    
    # Post management pages
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    
    # Support page URL
    path('support/', support_page, name='support_page'),
]