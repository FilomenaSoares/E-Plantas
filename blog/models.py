# Arquivo: blog/models.py

from django.db import models
from django.conf import settings # Importa as configurações para referenciar o CustomUser

# Modelo para as categorias dos posts
class PostCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nome da Categoria")
    slug = models.SlugField(max_length=100, unique=True, help_text="Usado para URLs amigáveis.")
    
    class Meta:
        verbose_name = "Categoria de Post"
        verbose_name_plural = "Categorias de Posts"
        ordering = ['name']
        
    def __str__(self):
        return self.name

# Modelo para os posts (Artigos e Dicas)
class Post(models.Model):
    class PostStatus(models.TextChoices):
        DRAFT = "DRAFT", "Rascunho"
        PENDING_REVIEW = "PENDING", "Pendente de Revisão"
        PUBLISHED = "PUBLISHED", "Publicado"

    POST_TYPE_CHOICES = [('ARTIGO', 'Artigo Científico'), ('DICA', 'Dica de Cultivo')]

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Autor"
    )
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Conteúdo")
    image = models.ImageField(upload_to='posts/', blank=True, null=True, verbose_name="Imagem de Destaque")
    post_type = models.CharField(max_length=10, choices=POST_TYPE_CHOICES, default='DICA', verbose_name="Tipo de Post")
    status = models.CharField(max_length=10, choices=PostStatus.choices, default=PostStatus.DRAFT, verbose_name="Status")
    
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_posts', blank=True)
    saves = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='saved_posts', blank=True)
    
    category = models.ForeignKey(PostCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")
    published_date = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=False, verbose_name="É destaque?")
    summary = models.TextField(blank=True, null=True, verbose_name="Resumo do Artigo")
    pdf_file = models.FileField(upload_to='articles_pdf/', blank=True, null=True, verbose_name="Arquivo PDF")
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-published_date']

    def __str__(self):
        return self.title

# Modelo para os comentários
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name="Comentário")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Comentário de {self.author} em {self.post}'
