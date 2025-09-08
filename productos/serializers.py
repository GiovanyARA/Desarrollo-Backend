from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'stock', 'creado', 'actualizado']
        read_only_fields = ['id', 'creado', 'actualizado']

    def validate_nombre(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("El nombre es requerido.")
        return value.strip()

    def validate_precio(self, value):
        if value is None:
            raise serializers.ValidationError("El precio es requerido.")
        if value <= 0:
            raise serializers.ValidationError("El precio debe ser mayor a 0.")
        return value

    def validate_stock(self, value):
        if value is None:
            raise serializers.ValidationError("El stock es requerido.")
        if value < 0:
            raise serializers.ValidationError("El stock debe ser mayor o igual a 0.")
        return value
