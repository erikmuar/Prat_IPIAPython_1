class Animal: 
    
    def __init__(self, edad, color):
        self.edad = edad 
        self.color = color
    
    def nacer(self):
        print("Este animal ha nacido ")

    def hablar(self):
        print("Este animal emite un sonido")



class Pajaro(Animal):
    
    def __init__(self, edad, color, altura_vuelo): # Creamos un init nuevo solo para pajaro, cuando crees un pajaro te pedira las 3 atributos
        self.edad = edad 
        self.color = color
        self.altura_vuelo = altura_vuelo
    
    
    def hablar(self):# Creamos otro modulo hablar para que sea especifico para pajaros
        print("pio")
        
    def volar(self,metros):
        print(f"El pajaro vuela una cantidad de {metros} metros")

piolin = Pajaro(2,"amarillo",60)

# Creamos nuevo animal, en este caso solo pedira 2 atributos
mi_animal = Animal(5,"negro")

mi_animal.hablar()     #Si escribimos mi_animal. vemos que no aparece el modulo volar porque solo es propio de los pajaros

piolin.nacer()
piolin.hablar()
piolin.volar(40)