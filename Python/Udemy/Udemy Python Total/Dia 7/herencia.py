# La herencia nos permite tener unos metodos y atributos que sean comunes de varias clases juntos para no tener que repetir la creacion de dichos metodos en cada uno de ellos.


class Animal: 
    
    def __init__(self, edad, color):
        self.edad = edad 
        self.color = color
    
    def nacer(self):
        print("Este animal ha nacido ")




class Pajaro(Animal):
    pass 

print(Pajaro.__bases__) # __bases__ Es una propiedad que me va a indicar de quien hereda esta clase, en este caso hereda de Animal

print(Animal.__subclasses__()) # __subclasses__ DIce a que subclases transmite su herencia la clase Animal, de momento solo a Pájaro


piolin = Pajaro(3,"amarillo")

piolin.nacer()

print(piolin.color)


#%% Practica 1 Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.

class Persona:

    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
class Alumno(Persona):
    pass

#%% Practica 2 Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.

class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas= cantidad_patas
    
    
class Perro(Mascota):
    pass


# %% Practica 3 Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo.


class Vehiculo: 
    
    def acelerar(self):
        pass
    def frenar(self):
        pass
    
class Automovil(Vehiculo):
    pass