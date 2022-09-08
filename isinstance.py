class Persona:
    nombre = 'eduardo'


class Animal:
    raza = 'gato siames'


obj1 = Persona()
obj2 = Animal()

print(isinstance(obj1, Persona))
print(isinstance(obj1, Animal))