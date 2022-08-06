# Operadores Arimeticos
# Suma (+)
suma = 5 + 4
# f-string, forma de imprimir concatenando variables
# 1º Forma
# print("La suma es: " + str(suma))
# 2º Forma
print(f"La suma es: {suma}")
# Resta (-)
resta = 5 - 2
print(f"La resta es: {resta}")
# Multiplicacion (*)
multiplicacion = 2 * 5
print(f"La multiplicacion es: {multiplicacion}")
# Division (/)
division = 10 / 5
print(f"La division es: {division}")
# Division Exacta (//)
division_exacta = 10 // 5
print(f"La division exacta es: {division_exacta}")
# Potencia (**)
potencia = 5 ** 2
print(f"La potencia es: {potencia}")
# Residuo / Modulo (%)
residuo = 24 % 5
print(f"El residuo es: {residuo}")

# Ejercicio
# Crear un archivo temperature.py, y dentro de ella vamos a convertir
# la temperatura de Lima -> Fº a Cº
# Formula:
# celsius = (farenheit - 32) / 1.8

# Ejercicio 2
# Crear un archivo imc.py y dentro de ella vamos a calcular
# el indice de masa corporal.
# Formula:
# imc = peso / altura ** 2

# Operadores de comporación
# ==  igual a
# !=  diferente a
# <  menor a
# <=  menor igual a
# >  mayor a
# >= mayor igual a
print(f"Son iguales:  {10 == 15}")
print(f"Son diferentes: {10 != 15}")
print(f"Es menor: {10 < 8}")
print(f"Es menor igual: {10 <= 10}")
print(f"Es mayor: {15 > 8}")
print(f"Es mayor igual: {15 >= 15}")

# Operadores logicos
# && -> and
# || -> or
# ! -> not
# TRUE - TRUE -> true

# (numero > 5) and (numero_2 < 5)

# Operadores de identidad (Strings)
# IGUAL Y DIFERENTE
# is -> es
# is not -> no es
# frutas = None
# print(frutas is None) -> True

# Ejercicio 3
# Crear un archivo llamado quadratic.py, vamos a formular
# ecuación cuadratica: ax**2 + bx + c = 0
a = 1
b = 2
c = 1

x1 = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
x2 = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)

print(x1, x2)