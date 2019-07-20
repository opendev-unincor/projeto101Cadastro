from django.db import models

# Create your models here.
class Pessoa(models.Model):
	nome = models.CharField('nome',max_length=50)