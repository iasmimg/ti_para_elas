from django.db import models

class Acao(models.Model):
    titulo = models.CharField('Título', max_length=100, blank=True, null=False)
    descricao = models.TextField(blank=True, null=False)
    autor = models.CharField('Autor', max_length=255, blank=True, null=False)
    tipo = models.CharField('Tipo', max_length=255, blank=True, null=False)
    imagem = models.ImageField(upload_to='imagens/', blank=True, null=True)
    linkgeral = models.URLField(blank=False, null=False)
    linkms = models.URLField(blank=True, null=False)