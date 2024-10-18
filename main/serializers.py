from rest_framework import serializers
from .models import Itens, funcionarios

class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itens
        #fields = '__all__'
        fields = ['id', 'nome', 'descricao', 'valor']


class  funcionariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = funcionarios
        fields = ['id', 'nome', 'cargo', 'salario']
