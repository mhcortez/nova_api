from django.db import models

class Itens(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    valor = models.FloatField()
    
    def __str__(self) -> str:
        return f'item: {self.nome}'

class funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    salario = models.FloatField()

    def __str__(self) -> str:
        return f'funcionario: {self.nome}'
    
    