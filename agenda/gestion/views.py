from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListAPIView

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


class PruebaApiView(ListAPIView):
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