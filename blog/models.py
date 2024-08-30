from django.db import models

# Create your models here.
class Interesses(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TimeField()
    nivel = models.FloatField()
    def __str__(self):
        return self.nome

class Cursos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    finalizacao = models.DateField()
    def __str__(self):
        return self.nome

class Jogos_favoritos(models.Model):
    nome = models.CharField(max_length=100)
    tema = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/')
    def __str__(self):
        return self.nome

