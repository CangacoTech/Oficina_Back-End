from django.db import models

class Curiosidade(models.Model):
    titulo = models.TextField()
    descricao = models.TextField()
