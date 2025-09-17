from django.db import models

# musicas/models.py
from django.db import models

class Musica(models.Model):
    nome = models.CharField(max_length=255)
    tom = models.CharField(max_length=255, blank=True)     
    cifra = models.CharField(max_length=255, default="")
    bpm = models.CharField(max_length=255, default="")
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']
        




