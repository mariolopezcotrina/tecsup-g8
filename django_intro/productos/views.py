from rest_framework import generics, status
from rest_framework.response import Response
from .models import Productos
from .serializers import ProductosSerializer

# Create your views here.


class ProductosView(generics.ListAPIView):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer

    def get(self, request):
        productos = self.get_serializer(self.get_queryset(), many=True)
        return Response(data=productos.data, status=status.HTTP_200_OK)