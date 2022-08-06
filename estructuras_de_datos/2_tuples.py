# Tuplas -> Inmutable | const
nombres = ("Luis", "Manuel", "Marco", "Mario")

# count -> cuenta las repeticiones de un valor en mención
luis_repeticiones = nombres.count("Luis")
print(f"count -> {luis_repeticiones}")

# index -> retorna el indice del valor a buscar
marco_indice = nombres.index("Marco")
print(f"index -> {marco_indice}")

#################################################
# list -> convertir en una lista
# print(nombres, type(nombres))
# print(list(nombres), type(list(nombres)))

nombres_lista = list(nombres)
nombres_lista.append("Martin")
print(f'append -> {nombres_lista}')

# tuple -> convertir en una tupla
nombres = tuple(nombres_lista)
print(f"nueva tupla -> {nombres}")
