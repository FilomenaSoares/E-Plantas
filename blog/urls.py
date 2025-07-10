from django.urls import path
from .views import like_post, save_post
from .views import (
    article_list_view,
    cultivation_tips_view,
    post_detail_view,
    UserPostListView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PendingPostsListView,
    approve_post,
    reject_post
)

app_name = 'blog'

urlpatterns = [

    path('artigos/', article_list_view, name='article_list'),
    path('dicas/', cultivation_tips_view, name='cultivation_tips'),
    path('post/<int:post_id>/', post_detail_view, name='post_detail'),
    
    path('meus-posts/', UserPostListView.as_view(), name='my_posts'),
    path('post/novo/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/editar/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/apagar/', PostDeleteView.as_view(), name='post_delete'),

    path('moderacao/pendentes/', PendingPostsListView.as_view(), name='pending_posts'),
    path('moderacao/aprovar/<int:pk>/', approve_post, name='approve_post'),
    path('moderacao/rejeitar/<int:pk>/', reject_post, name='reject_post'),
    path('post/<int:pk>/like/', like_post, name='like_post'),
    path('post/<int:pk>/save/', save_post, name='save_post'),
]