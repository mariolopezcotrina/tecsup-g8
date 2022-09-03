from rest_framework import serializers
from .models import Importancia

class PruebaSerializer(serializers.Serializer):
    # ahora vamos a definir la informacion que va a llegar y/o salir
    # https://www.django-rest-framework.org/api-guide/fields/
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(required=True, trim_whitespace= True, max_length= 20)
    apellido = serializers.CharField(required=True, trim_whitespace= True, max_length= 15)
    password = serializers.CharField(write_only=True)

    def create(self, data_validada):
        print('Aca se deberia de guardar la info en la BD')
        print(data_validada)
        # aca se deberia de retorna esa informacion guardada en la bd
        return 


class ImportanciaSerializer(serializers.ModelSerializer):

    def save(self):
        # modifico el nombre de la data_validad y lo convierto a minusculas
        self.validated_data['nombre'] = self.validated_data.get('nombre').lower()

        nuevaImportancia = Importancia.objects.create(**self.validated_data)

        return nuevaImportancia
        
    class Meta:
        model = Importancia # para poder setear todos los fields de mi modelo en el serializador
        # fields > sirve para indicar que columnas del modelo vamos a utilizar en este serializar
        fields = '__all__'


class ImportanciaSerializerRUD(serializers.ModelSerializer):
    class Meta:
        model = Importancia 
        fields = '__all__'