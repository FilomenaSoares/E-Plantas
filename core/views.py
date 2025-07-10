# Arquivo: core/views.py

from django.shortcuts import render
from blog.models import Post

def homepage(request):

    featured_articles = Post.objects.filter(is_featured=True, post_type='ARTIGO')[:2]
    featured_tips = Post.objects.filter(is_featured=True, post_type='DICA')[:2]
    featured_items = list(featured_articles) + list(featured_tips) 
    
    recent_posts = Post.objects.order_by('-published_date')[:3]

    context = {
        'featured_items': featured_items,
        'recent_posts': recent_posts, 
    }
    
    return render(request, 'core/homepage.html', context)
