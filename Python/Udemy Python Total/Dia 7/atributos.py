class Pajaro: 
    
    alas = True #Esto aplica a todos los "pajaros" que creemos
    
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie
        
mi_pajaro = Pajaro("negro","colibri")

print(f"Mi pajaro es un {mi_pajaro.especie} y es de color {mi_pajaro.color}")   

print(Pajaro.alas)