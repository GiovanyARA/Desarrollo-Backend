from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator

class Producto(models.Model):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]  # > 0
    )
    stock = models.IntegerField(
        validators=[MinValueValidator(0)]  # >= 0
    )
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-creado']  # orden por defecto (más reciente primero)

    def __str__(self):
        return f"{self.nombre} (${self.precio})"
