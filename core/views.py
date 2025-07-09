# Arquivo: core/views.py

from django.shortcuts import render
from blog.models import Post

def homepage(request):
    """
    View para a página inicial.
    Busca os destaques, combina-os em uma única lista ordenada,
    busca os produtos recentes e também as postagens mais recentes do blog.
    """
    # 1. Busca artigos científicos em destaque
    featured_articles = Post.objects.filter(is_featured=True, post_type='ARTIGO')[:2]

    # 2. Busca dicas de cultivo em destaque
    featured_tips = Post.objects.filter(is_featured=True, post_type='DICA')[:2]


    
    # 4. Combina todos os itens de destaque em uma única lista, mantendo a ordem
    featured_items = list(featured_articles) + list(featured_tips) 
    


    # 6. Busca as 3 postagens mais recentes do blog (artigos ou dicas)
    recent_posts = Post.objects.order_by('-published_date')[:3]

    context = {
        'featured_items': featured_items,
        'recent_posts': recent_posts, # Adiciona as postagens recentes ao contexto
    }
    
    return render(request, 'core/homepage.html', context)
