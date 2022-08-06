# Diccionarios
# { key: value } -> objeto o json
alumno = {
    "nombre": "Eddy",
    "apellidos": "Valencia Guillen",
    "especialidades": [
        {
            "nombre": "Frontend"
        },
        {
            "nombre": "Backend"
        }
    ]
}

print(f"Obtener el nombre -> {alumno['nombre']}")
print(f"Obtener la segunda especialidad -> {alumno['especialidades'][1]}")

# items -> retornar lista de tuplas con 2 valores (key, value)
print(f"items -> {alumno.items()}")

# keys -> retorna una lista con todas los keys
print(f"keys -> {alumno.keys()}")

# values -> retorna una lista con todos los valores
print(f"values -> {alumno.values()}")

# Si no existe un key, podemos crearlo
alumno['edad'] = 25
print(alumno)

# get -> busca el key mencionado, si no lo encuentra retorna un valor None
print(f"get -> {alumno.get('signo')}")

# pop -> eliminar el key con su valor
alumno.pop('edad')
print(f'pop -> {alumno}')
