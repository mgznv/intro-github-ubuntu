from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
	titulo = models.CharField(max_length = 140)
	categoria_id = models.IntegerField()

class Enlace(models.Model):
	titulo = models.CharField(max_length= 140)
	enlace = models.URLField()
	votos = models.IntegerField(default = 0)
	categoria = models.ForeignKey(Categoria)