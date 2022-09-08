from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PruebaSerializer, ImportanciaSerializer, ImportanciaSerializerRUD
from .models import Importancia

# Tipado > indicar a determinadas variables su tipo de dato correspondiente
@api_view(http_method_names=['GET', 'POST'])
def endpointInicial(request: Request):
    print(request.method)
    # request > sera toda la informacion enviada por el cliente
    if request.method == 'GET':
        return Response(data={
            'message': 'Bienvenido a mi API'
        }, status=200)

    elif request.method == 'POST':
        print(request.data)

        return Response(data={
            'message':'Se creo la informacion correctamente'
        })


class PruebaApiView(ListCreateAPIView):
    # 2 atributos : queryset y serializer_class
    queryset = [
        {
            'id': 1, 
            'nombre': 'eduardo', 
            'apellido': 'de rivero'
        }, 
        {
            'id': 2, 
            'nombre': 'fiorella', 
            'apellido': 'marquez'
        }]
    serializer_class = PruebaSerializer

    def post(self, request: Request):
        # Si quisieramos modificar el funcionamiento automatico que nos brinda las vistas genericas lo podemos hacer declarando el metodo con el mismo nombre del metodo que queremos modificar
        data = self.serializer_class(data=request.data)
        validacion = data.is_valid()
        print(validacion)

        if validacion == True:
            # la data para guardar en la bd
            print(data.validated_data)
            # la data que sera devuelta para el usuario
            print(data.data)
            return Response(data={
                'message': 'Prueba creada exitosamente'
            }, status=201)
        else:
            return Response(data={
                'message': 'Error al crear la prueba',
                'content': data.errors
            }, status=400)


class ImportanciasView(ListCreateAPIView):
    queryset = Importancia.objects.all() # SELECT * FROM importancia;
    serializer_class = ImportanciaSerializer
    
    def get_queryset(self):
        # SELECT * FROM importancias WHERE delete = false;
        return self.queryset.filter(deleted=False).all()

    def get(self, request: Request):
        instancias = self.get_queryset() 
        # print(instancias[0].nombre)
        for instancia in instancias:
            print(instancia.nombre)
        # cuando tenemos ya la informacion de la base de datos entonces seran instancias (registros), en cambio cuando tenemos la informacion a guardar en la bd y queremos validar que este correcta lo pasaremos mediante data, instance espera una o varias instancias, data espera informacion
        data_serializada = self.serializer_class(instance= instancias, many=True)

        return Response ({
            'message': 'Las instancias son',
            'content': data_serializada.data
        })
    
    def post(self, request: Request):
        informacion = request.data # Informacion extraida del body
        dataASerializar = self.serializer_class(data=informacion)

        dataASerializar.is_valid(raise_exception=True)

        nuevaImportancia = dataASerializar.save() # guarda la informacion en la base de datos

        ###

        # # Primera forma de guardado de la informacion en la base de datos usando el modelo directamente
        # infoImportancia = {'nombre':'Ejemplo'}
        # Importancia.objects.create(**infoImportancia) 

        # # Segunda forma
        # nuevaImportancia = Importancia(**infoImportancia)
        # nuevaImportancia.save()

        ###

        return Response({
            'message':'Importancia creada exitosamente',
            'content': self.serializer_class(instance=nuevaImportancia).data
        }, status=201)


# GET, PUT, DELETE
class ImportanciaView(RetrieveUpdateDestroyAPIView):
    queryset = Importancia.objects.all()
    serializer_class=ImportanciaSerializerRUD

    def validarImportancia(self, pk):
        # SELECT * FROM importancias WHERE id = ... and deleted = false LIMIT 1;
        resultado = Importancia.objects.filter(id=pk, deleted= False).first()

        if resultado is None:
            return Response(data={
                'message': 'Importancia no existe',
                'content': None
            }, status = 404)
        return resultado

    def get(self, request, pk):
        # Si modifico el nombre en la ruta entonces tbn lo tendre que modificar como parametro del metodo
        print(pk)
        resultado = self.validarImportancia(pk)
        # isinstance(instancia, Clase) > retornara boolean si la instancia pertenece o no pertenece a esa clase
        if isinstance(resultado, Response):
            return resultado
        else:
            # aca enviamos la instancia para transformar la data a una informacion que el cliente la pueda entender
            dataSerializada = self.serializer_class(instance=resultado).data

            return Response(data={
                'message': None,
                'content': dataSerializada
            })
    
    def delete(self, request, pk):
        resultado = self.validarImportancia(pk)
        if isinstance(resultado, Response):
            return resultado
        else:
            resultado.deleted = True
            resultado.save()
            return Response(data={
                'message': 'Importancia eliminada exitosamente',
                'content': None
            })
    
    def update(self, request, pk):
        resultado = self.validarImportancia(pk)

        if isinstance(resultado, Response):
            return resultado

        else:
            # pasamos la informacion enviada por el body hacia el serializador
            dataSerializada = self.serializer_class(data=request.data)

            # validamos que la informacion sea valida
            dataSerializada.is_valid(raise_exception=True)

            # aca se actualiza la informacion de la importancia
            # retorna la instancia actualizada
            importanciaActualizada = dataSerializada.update(resultado, dataSerializada.validated_data)
            
            # retornamos la importacia actualizada
            return Response(data={
                'message': 'Importancia actualizada exitosamente',
                'content': self.serializer_class(instance=importanciaActualizada).data  #dataSerializada.data # va a ser la informacion que he pasado al momento de llamar al serializador  
            })