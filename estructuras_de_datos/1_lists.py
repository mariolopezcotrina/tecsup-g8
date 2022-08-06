# Estructura de datos
# Lista -> Array / Arreglo | var o let
#               1       2       3       4           5 -> Posición
#               0       1       2       3           4 -> Indice
personas = ["Claudia", "Diego", "Eddy", "Fernando", "Flavio"]
# n - 1
print(f"La persona en la posición 3 es: {personas[2]}")
print(f"La persona en el indice 4 es: {personas[4]}")

# Metodos -> Esta función puede ser llamada si existe una variable en memoria.
# Funciones -> Existe de manera global y es llamada sin instanciarla.

# append -> agregar un valor a una lista
personas.append("Gerardo")
print(f"append -> {personas}")

# insert -> inserta un valor en un indice definido
personas.insert(0, "Javier")
print(f"insert -> {personas}")

# index -> retornar el indice del valor mencionado
indice_fernando = personas.index("Fernando")
print(f"index Fernando -> {indice_fernando}")

# extend -> unir dos listas
personas_nuevas = ["Jherry", "John", "Jorge", "José"]
personas.extend(personas_nuevas)
print(f"extend -> {personas}")

# remove -> elimina un valor de la lista
personas.remove("John")
print(f"remove -> {personas}")

# pop -> elimina el valor segun el indice
personas.pop(4)
print(f"pop -> {personas}")

# sort -> ordernar valores de una lista
personas.sort(reverse=False) # reverse = True, se ordena de mayor a menor
print(f"sort -> {personas}")

# count -> contar cuantas veces existe el valor en mención
# personas.append("Flavio") -> Se agrega para validar que funciona
flavio_repetidos = personas.count("Flavio")
print(f"count -> {flavio_repetidos}")

# len -> cuenta los elementos de una estructura de datos | length
print(f"Total de personas: {len(personas)}")
