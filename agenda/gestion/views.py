from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView, ListCreateAPIView
from .serializers import PruebaSerializer

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