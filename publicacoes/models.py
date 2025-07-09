from django.db import models

class CategoriaPublicacao(models.Model):
    nome = models.CharField(max_length=100)

class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    imagem = models.ImageField(upload_to='publicacoes/', blank=True, null=True)
    categoria = models.ForeignKey(CategoriaPublicacao, on_delete=models.SET_NULL, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
