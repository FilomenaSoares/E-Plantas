# Em blog/admin.py

from django.contrib import admin
from .models import PostCategory, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_type', 'author', 'category', 'published_date', 'is_featured')
    list_filter = ('post_type', 'is_featured', 'category')
    search_fields = ('title', 'content', 'author')
    date_hierarchy = 'published_date'

    # Organiza os campos em seções para melhor usabilidade
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('title', 'post_type', 'is_featured', 'image')
        }),
        ('Conteúdo Principal', {
            'fields': ('content',),
            'description': 'Para Artigos, este campo pode ser usado como uma introdução ou chamada.'
        }),
        ('Detalhes do Artigo Científico', {
            'classes': ('collapse',), # Começa recolhido
            'fields': ('author', 'summary', 'pdf_file'),
            'description': 'Preencha estes campos apenas se o "Tipo de Post" for "Artigo Científico".'
        }),
        ('Detalhes da Dica de Cultivo', {
            'classes': ('collapse',),
            'fields': ('category',),
            'description': 'Selecione uma categoria se o "Tipo de Post" for "Dica de Cultivo".'
        }),
    )

admin.site.register(PostCategory)
admin.site.register(Post, PostAdmin)
