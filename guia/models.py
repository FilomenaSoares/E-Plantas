from django.db import models


class Planta(models.Model):
    nome_popular = models.CharField(max_length=100)
    nome_cientifico = models.CharField(max_length=200, blank=True)
    imagem = models.ImageField(upload_to='plantas/')
    descricao = models.TextField()

class GuiaPlantio(models.Model):
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    epoca_plantio = models.CharField(max_length=100)
    solo_ideal = models.CharField(max_length=100)
    rega = models.TextField()
    iluminacao = models.TextField()
    passos = models.TextField()
