from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import ItensViewSet, funcionariosViewSet


router = DefaultRouter()
router.register(r'itens', ItensViewSet)
router.register(r'funcionarios', funcionariosViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
