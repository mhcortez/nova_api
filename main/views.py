from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Itens, funcionarios
from .serializers import ItensSerializer , funcionariosSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ItensViewSet(viewsets.ModelViewSet):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer
    #permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','nome']

class funcionariosViewSet(viewsets.ModelViewSet):
    queryset = funcionarios.objects.all()
    serializer_class = funcionariosSerializer
    #permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id','nome']
