class Pajaro: 
    alas = True # Atributo de clase
    
    def __init__(self,color,especie):
        self.color= color #Atributo de instancia
        self.especie = especie # Atributo de instancia
    
    def piar(self): #SIEMPRE hay que poner el parametro self de forma obligatoria 
        print("pio")
            
    def volar(self,metros):  #SIEMPRE hay que poner el parametro self de forma obligatoria 
        print(f"El pajaro vuela {metros} metros.")


piolin = Pajaro("amarillo","canario")

piolin.piar()

piolin.volar(50)



#%% Practica Métodos 1 
# Crea una clase Perro. Dicho perro debe poder ladrar.

#Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".

class Perro:
    
    def ladrar(self): 
        print("Guau!")
    

Toby = Perro()

Toby.ladrar()

#%% Practica Metodos 2 
#Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").

#Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.

class Mago:
    
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
        
merlin = Mago()

merlin.lanzar_hechizo()


#%% Practica Metodos 3 
#Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje

# "La alarma ha sido pospuesta {cantidad_minutos} minutos"

class Alarma: 
    
    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")


reloj = Alarma()

reloj.postergar(50)

