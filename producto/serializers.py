from rest_framework import serializers

from .models import Productos

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ('id', 'referencias', 'nombre', 'descripcion', 'fechaIngreso')
        read_only_fields = ('fechaIngreso',)