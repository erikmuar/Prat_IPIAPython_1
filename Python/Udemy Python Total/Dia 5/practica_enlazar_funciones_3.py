import random

def lanzar_moneda():
    
    cara_cruz = random.choice(["Cara","Cruz"])
    
    return cara_cruz
        
lista_numeros = [1,4,7,22,90,31]

def probar_suerte(cara_cruz,lista_numeros):
    
    if cara_cruz == "Cara":
        print("La lista se autodestruirá")
        lista_numeros.clear()
    
        
    elif cara_cruz == "Cruz":
        print("La lista fue salvada")
    
    return lista_numeros