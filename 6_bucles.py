# for -> foreach

meses = ["Enero", "Febrero", "Marzo", "Abril"]

# for mes in meses:
#     print(mes)

# Obtener el indice, valor dentro de una iteración
# for index, mes in enumerate(meses):
#     print(index, mes)

# range -> recibi 3 parametros
# 1ª donde empieza
# 2ª hasta donde finaliza
# 3ª cuanto en cuanto incrementa
# for(let i=0; i<10; i++) {....}

# for numero in range(1, 10, 2):
#     print(numero)

# Ejemplo 2
alumno = {
    "nombre": "Fernando",
    "apellidos": "Cangana",
    "cursos": ["Algebra", "Aritmetica"]
}

# for key in alumno:
#     if key == 'cursos':
#         for curso in alumno[key]:
#             print(curso)

# While (mientras)
edad = 25

while edad > 18:
    print(f'actual -> {edad}')
    edad -= 1
    
    if edad == 21:
        break
