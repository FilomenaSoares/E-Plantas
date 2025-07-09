from django.db import models


class CategoriaProduto(models.Model):
    nome = models.CharField(max_length=100)

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.PositiveIntegerField()
    imagem = models.ImageField(upload_to='produtos/')
    categoria = models.ForeignKey(CategoriaProduto, on_delete=models.SET_NULL, null=True)

class Pedido(models.Model):
    nome_cliente = models.CharField(max_length=100)
    email = models.EmailField()
    data_pedido = models.DateTimeField(auto_now_add=True)
    produtos = models.ManyToManyField(Produto, through='ItemPedido')

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
