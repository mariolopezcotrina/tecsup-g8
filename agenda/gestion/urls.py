from django.urls import path
from .views import endpointInicial, PruebaApiView, ImportanciasView, ImportanciaView

urlpatterns = [
    path('inicio', endpointInicial),
    path('prueba', PruebaApiView.as_view()),
    path('importancias', ImportanciasView.as_view()),
    path('importancia/<int:pk>', ImportanciaView.as_view()) # primary key
]