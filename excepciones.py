# try catch -> try except
# try:
#     numero = int(input('Ingresa un número: '))
#     if numero < 0:
#         # print('El numero ingresado es menor a 0')
#         raise Exception('El numero ingresado es menor a 0')
#     resultado = (numero + 10) / 2
#     print(resultado)
# except ValueError:
#     print('El valor ingresado no es un número, intente nuevamente')
# except ZeroDivisionError:
#     print('La división no se puede realizar con el número 0')
# except KeyboardInterrupt:
#     print('\nLa aplicación se detuvo')
# except Exception as e:
#     print(e.__class__)
#     print(e)

# finally
# else
#try:
#    print(10/2)
#except Exception:
#    print('Error')
#else:
#    print('Else')
#finally:
#    print('Finally')


# Ejercicio
# Crear un programa que nos pida ingresar un número entero, dicho número
# debe llegar a 1 usando la serie de Collatz
# 19 ------------------------ 1
# si el numero es par, se divide entre dos
# si el numero es impar, se multiplica por 3 y se suma 1
# la serie termina cuando llega al número 1
# Ejemplo
# 19 58 29 88 ........ 1

# Extra
# Agregarle nuestro try except, y si existe un error no cierre el programa, pero si
# muestre el error

while True:
    try:
        numero = int(input('Ingrese el número inicial: '))
        
        if numero < 0:
            raise Exception('El número ingresado debe ser mayor a 1')
        
        while numero != 1:
            if numero % 2 == 0:
                numero //= 2
            else:
                numero = (numero * 3) + 1
            print(numero)
    except ValueError:
        print('El valor ingresado no es un número')
    except Exception as e:
        print(e)
    else:
        break
