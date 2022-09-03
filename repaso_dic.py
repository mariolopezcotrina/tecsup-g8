persona = {'nombre': 'Eduardo', 'apellido': 'juarez', 'sexo': 'Masculino'}

# print(persona['sexo'])
# el metodo get intentara buscar esa llave y si no la encuentra retornara None, de otro modo podemos colocar un valor por defecto
print(persona.get('sexo', 'No binario'))