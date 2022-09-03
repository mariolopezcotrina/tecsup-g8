from django.urls import path
from .views import endpointInicial, PruebaApiView

urlpatterns = [
    path('inicio', endpointInicial),
    path('prueba', PruebaApiView.as_view())
]