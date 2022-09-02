from django.urls import path
from .views import endpointInicial

urlpatterns = [
    path('inicio', endpointInicial)
]