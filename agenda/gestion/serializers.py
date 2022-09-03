from rest_framework import serializers

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