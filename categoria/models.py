from django.db import models

# Create your models here.
class Categoria(models.Model):
    Categoria_nome = models.CharField(max_length=100, unique=True)
    Categoria_descricao = models.TextField(max_length=300, blank=True)
    Categoria_imagem = models.ImageField(upload_to='fotos/categorias', blank=True)

