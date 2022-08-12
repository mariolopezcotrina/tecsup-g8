# Ejercicio 1
## Crea un programa que valide si la palabra ingresada
## es un palindromo
# Lista
# For
# lista con funcion insert
# funcion join (cadena de texto) -> investigación

# Solución 1
# letras_invertidas = []
#palabras = input("Ingrese la palabra a validar: ")
# 
# for letra in palabras:
#     letras_invertidas.insert(0, letra)
# 
# palabra_invertida = ''.join(letras_invertidas)

# Solución 2
#palabra_invertida = palabras[::-1]
#
#if palabras == palabra_invertida:
#    print('Es un palindromo')
#else:
#    print('No es un palindromo')

## Ejercicio 2
# Crea un programa donde ingreses tu año de nacimiento, 
# este mismo se va a iterar restandole el año actual
# de tal manera nos va a ir imprimiendo el año y la edad que tenias en dicho año
# 1994
# 2022
# 28
# 1995 tenia 1 años
# 1996 tenia 2 años
# .....
# 2022 tengo 28 años
## while -> excepciones
## input
## for
## if

#anio_actual = 2022
#anio_nacimiento = int(input('Ingresa el año en el que naciste: '))
#
#if anio_nacimiento < anio_actual:
#    edad = anio_actual - anio_nacimiento
#    for i in range(edad):
#        edad_anterior = i + 1
#        if (anio_nacimiento + edad_anterior) == anio_actual:
#            print(f'Actualmente en el año {anio_actual} tienes {edad_anterior} años')
#        else:
#            print(f'En el año {anio_nacimiento + edad_anterior} tenias {edad_anterior} años')
#else:
#    print(f'El año de nacimiento no debe ser mayor a {anio_actual}')
#

## Ejercicio 3
## Crea un programa donde te pida ingresar: altura y ancho de un rectangulo
## posterior a ello vamos a dibujar el rectangulo, tomando como signo *
## altura: 5
## ancho: 4
# ****
# ****
# ****
# ****
# ****
# for
# range
# print -> argumento end
altura = int(input('Ingrese la altura: '))
ancho = int(input('Ingrese el ancho: '))

for _ in range(altura):
    for _ in range(ancho):
        print('*', end='')
    print('')
