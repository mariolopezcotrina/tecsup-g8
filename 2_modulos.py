# npm -> npm install
# node_modules

# Entornos virtuales
## Crear un entorno virtual
## python -m venv venv

## Activar nuestro entorno
### Git Bash -> Windows
## source venv/Scripts/activate
### Git Bash -> MacOs - Linux
## source venv/bin/active
### Terminal de Windows - Power
## cd venv
## cd Scripts
## activate.bat / activate.ps1

# Desactivar entorno virtual
# deactivate

# Instalar dependencia
# pip install nombre_paquete

# Desinstalar dependencia
# pip uninstall nombre_paquete

# Crear nuestro archivo de dependencias
# pip freeze > requirements.txt

# Instalar las dependencias del archivo requirements.txt
# pip install -r requirements.txt
#import camelcase
from camelcase import CamelCase as CamelCaseClase
from funciones import ejercicio2

instancia = CamelCaseClase()
text = "hola chicos"
print(instancia.hump(text))

ejercicio2(
    {'nombre': 'Claudia', 'nota': 15}, {'nombre': 'Diego', 'nota': 14},
    {'nombre': 'Eddy', 'nota': 16}, {'nombre': 'Fernando', 'nota': 10},
    {'nombre': 'Flavio', 'nota': 12}
)