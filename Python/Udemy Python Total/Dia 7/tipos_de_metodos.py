# Decoradores Métodos de instancia


class Pajaro: 
    alas = True # Atributo de clase
    
    def __init__(self,color,especie):
        self.color= color 
        self.especie = especie 
    
    def piar(self): #Metodo de instancia pòrque son metodos que afectan al self
        print("pio")
            
    def volar(self,metros):  #Metodo de instancia. 
        print(f"El pajaro vuela {metros} metros.")
        self.piar() # Modificamos el metodo de instancia para que a parte de volar llame a otro metodo, en este caso piar.

    def pintar_negro(self): # Estos metodos de instancia es capaz de acceder y modificar los atributos del objeto(piolin), con este metodo cambiamos el color a negro
        self.color = "negro"
        print(f"Ahora el color del pajaro es {self.color}")
        
        
    
piolin = Pajaro("amarillo","canario")

piolin.pintar_negro()


piolin.volar(40)

piolin.alas = False  #Con esto podemos modificar algo que afecta a toda la clase como es alas 




# Decoradores metodos de clase 


class Pajaro: 
    alas = True # Atributo de clase
    
    def __init__(self,color,especie):
        self.color= color 
        self.especie = especie 
    
    def piar(self): #Metodo de instancia pòrque son metodos que afectan al self
        print("pio")
            
    def volar(self,metros):  #Metodo de instancia. 
        print(f"El pajaro vuela {metros} metros.")
        self.piar() # Modificamos el metodo de instancia para que a parte de volar llame a otro metodo, en este caso piar.

    def pintar_negro(self): # Estos metodos de instancia es capaz de acceder y modificar los atributos del objeto(piolin), con este metodo cambiamos el color a negro
        self.color = "negro"
        print(f"Ahora el color del pajaro es {self.color}")
        
        
    @classmethod  # En los classmethods no se pone self sino cls, Este metodo al ser de clase y no de instancia no puede acceder a los atributos de instancia (color y especie)
    def poner_huevos(cls, cantidad):
        print(f"El pajaro puso {cantidad} de huevos")
        print(f"Es de color{self.color}") # no permite poner self.color porque solo 
        cls.alas = False #Esto funciona porque es un metodo  de clase y no de instancia
        print(Pajaro.alas)
        
    
Pajaro.poner_huevos(3)
Pajaro.piar()




# Decorador de metodos Estaticos

class Pajaro: 
    alas = True # Atributo de clase
    
    def __init__(self,color,especie):
        self.color= color 
        self.especie = especie 
    
    def piar(self): #Metodo de instancia pòrque son metodos que afectan al self
        print("pio")
            
    def volar(self,metros):  #Metodo de instancia. 
        print(f"El pajaro vuela {metros} metros.")
        self.piar() # Modificamos el metodo de instancia para que a parte de volar llame a otro metodo, en este caso piar.

    def pintar_negro(self): # Estos metodos de instancia es capaz de acceder y modificar los atributos del objeto(piolin), con este metodo cambiamos el color a negro
        self.color = "negro"
        print(f"Ahora el color del pajaro es {self.color}")
        
        
    @classmethod  # En los classmethods no se pone self sino cls, Este metodo al ser de clase y no de instancia no puede acceder a los atributos de instancia (color y especie)
    def poner_huevos(cls, cantidad):
        print(f"El pajaro puso {cantidad} de huevos")
        print(f"Es de color{self.color}") # no permite poner self.color porque solo 
        cls.alas = False #Esto funciona porque es un metodo  de clase y no de instancia
        print(Pajaro.alas)
        
    @staticmethod # Estos metodos estaticos no pueden acceder  ni a la clase ni a la instancia ni se puede modificar los atributos de clase ni instancia
    def mirar():
        print("El pajaro mira")

Pajaro.mirar()


#Práctica Tipos de Métodos 2
#Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.


class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True