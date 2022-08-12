## function nombre_funcion() { // logica de funcion }

## Variable -> unidad_de_medida -> SnakeCase
## Variable -> UNIDAD_DE_MEDIDA
## Funciones -> nombreFuncion
## Clases -> NombreClase

# Función en python
# def nombreFuncion():
#     pass

# Función con parametro
def saludar(nombre):
    print(f'Hola {nombre}, como estas?')
    
# Función con parametros opcionales o por defecto
def saludarConNombre(apellido='Cruz', edad=22, nombre='Juan'):
    print(f'{nombre} {apellido}, tu edad es: {edad}')

# saludarConNombre(nombre='Manuel', apellido='Ytuza', edad='26')

# Ejercicio
# Crear una función que reciba dos numeros y si la suma de ambos es par,
# hallar su mitad y si es impar, retornar el resultado de la suma
def ejercicio1(n1, n2):
    suma = n1 + n2
    if suma % 2 == 0:
        print(suma/2)
    else:
        print(suma)

# Función con multiparametros o multiargumentos
# *args -> obtenemos una tupla con los valores mencionados
# **kwargs -> obtenemos un diccionario con la mención key=value

#def alumnosInscritos(*args):
#    print(args)
#    
#alumnosInscritos('Claudia', 'Diego', 'Eddy', 'Fernando')

#def alumnosInscritos(**kwargs):
#    print(kwargs)
#
#alumnosInscritos(alumno_1='Claudia', alumno_2='Diego', alumno_3='Eddy')

# Ejercicio 2
# Crear una función que reciba N alumnos y este indique cuantos aprobaron y 
# cuantos desaprobaron
# nota > 10 -> Aprobado
# {"nombre": "", "nota": 0}
# ejercicio2({"nombre": "", "nota": 0}, {"nombre": "", "nota": 0})
# def
# for
# if
# *args
def ejercicio2(*args):
    aprobados = 0
    desaprobados = 0
    
    for alumno in args:
        if alumno['nota'] > 10:
            aprobados += 1
        else:
            desaprobados += 1
            
    print(
        f'Hay {aprobados} aprobados y {desaprobados} desaprobados '
        f'de un total de {len(args)} alumnos'
    )
    

#ejercicio2(
#    {'nombre': 'Claudia', 'nota': 15}, {'nombre': 'Diego', 'nota': 14},
#    {'nombre': 'Eddy', 'nota': 16}, {'nombre': 'Fernando', 'nota': 10},
#    {'nombre': 'Flavio', 'nota': 12}
#)