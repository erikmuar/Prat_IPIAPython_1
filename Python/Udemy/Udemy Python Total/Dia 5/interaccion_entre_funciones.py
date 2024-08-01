from random import *


# Crear una lista inicial que tenga los palitos que hay 

palitos = ["-","--","---","----"]

# Creamos una funcion que mezcle los palitos 

def mezclar(palitos):
    shuffle(palitos)
    return palitos



# Otra funcion que pida al usuario que elija un numero 


def probar_suerte():
    
    intento = ""
    while intento not in ["1","2","3","4"]:
        intento = input("Elige un número del 1 al 4: ")

    return int(intento)


# Crear funcion que compruebe el intento 


def comprobar_intento(palitos, intento):
    if palitos[intento-1]== "-":
        print("Has perdido")
    else:
        print("Te has salvado")
      
        
    

palitos_mezclados = mezclar(palitos)
intento = probar_suerte()

comprobar_intento(palitos_mezclados,intento)