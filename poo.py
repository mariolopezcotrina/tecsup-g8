# Clases en python
# Encapsulación
class Mueble:
    color = ''
    tipo = ''
    material = ''
    precio = 0.00
    
    # Toda función dentro de una clase, se le denomina como metodo
    def indicarTipo(self):
        return f'El tipo es: {self.tipo}'
    
# Mueble -> Sofa Cama
# Mueble -> Silla

# Abstracción
# instancia -> objeto
# mueble_1 = Mueble()
# mueble_1.tipo = 'Sofa Cama'
# print(mueble_1.indicarTipo())
# 
# mueble_2 = Mueble()
# mueble_2.tipo = 'Silla'
# print(mueble_2.indicarTipo())

# Clase con constructor
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.mascotas = ['perro', 'gato']
        
    def saludar(self):
        print(f'Hola, {self.nombre}')
        
    def __str__(self):
        return f'{self.nombre}, Instancia del objeto'

#persona_1 = Persona('Claudia', 26)
#persona_2 = Persona('Eddy', 24)

# persona_1.saludar()
# persona_2.saludar()

#print(persona_1)
#print(persona_2)

# Getter y setter
class Usuario:
    def __init__(self, usuario, contrasenia):
        self.usuario = usuario
        self.contrasenia = self.__encriptarContrasenia(contrasenia)
        self.__situacion_sentimental = 'Soltero'
        
    # Primera Forma
    # def __getSituacionSentimental(self):
    #     return self.__situacion_sentimental
    # 
    # def __setSituacionSentimental(self, situacion_sentimental):
    #     self.__situacion_sentimental = situacion_sentimental
    #     
    # situacion_sentimental = property(__getSituacionSentimental, __setSituacionSentimental)
        
    # Segunda forma
    @property
    def situacion_sentimental(self):
        return self.__situacion_sentimental
    
    @situacion_sentimental.setter
    def situacion_sentimental(self, situacion_sentimental):
        self.__situacion_sentimental = situacion_sentimental

    def __encriptarContrasenia(self, password):
        return f'$!$!$!$!$!$!{password}$!..4.213·"!'
        
usuario_1 = Usuario('martin', 'fiufiu')
# print(usuario_1.contrasenia)
print(usuario_1.situacion_sentimental)
usuario_1.situacion_sentimental = 'Conviviente'
print(usuario_1.situacion_sentimental)
