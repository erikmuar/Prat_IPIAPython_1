<<<<<<< HEAD
def reducir_lista(lista_numeros):
    
    lista_sin_duplicados = list(set(lista_numeros))
    
    print(lista_sin_duplicados)
    
    lista_ordenada = lista_sin_duplicados.sort()
    
    print(lista_ordenada)
    
    lista_sin_max = lista_ordenada.pop()
    
    print(lista_sin_max)
    
    return lista_sin_max

reducir_lista([2,4,6,15,6,5])
=======
from random import *


def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return print(dado1, dado2 )
    
    

def evaluar_jugada(dado1,dado2):
    suma_dados = dado1+dado2
    if suma_dados <= 6:
        print(f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados< 10: 
        print(f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados >= 10: 
        print(f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")
>>>>>>> 86624db1e242838f2372ba54282444811d331801
