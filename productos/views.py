from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, filters
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    # Ordenamiento: ?ordering=precio  | ?ordering=-precio  | ?ordering=nombre
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['precio', 'stock', 'nombre', 'creado', 'actualizado']
    ordering = ['-creado']  # igual que Meta.ordering del modelo
