from django.db import models

class Itens(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.FloatField()
    
    def __str__(self) -> str:
        return f'item: {self.nome}'
    
    