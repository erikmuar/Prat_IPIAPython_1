lista_numeros = [2,4,6,15,6,5]

def reducir_lista(lista_numeros):
    # Eliminar duplicados
    lista_sin_duplicados = list(set(lista_numeros))
    
    # Imprimir la lista sin duplicados
    print("Lista sin duplicados:", lista_sin_duplicados)
    
    # Ordenar la lista sin duplicados
    lista_sin_duplicados.sort()
    
    # Imprimir la lista ordenada
    print("Lista ordenada:", lista_sin_duplicados)
    
    # Eliminar el máximo valor de la lista usando pop()
    lista_sin_duplicados.pop()  # Esto elimina el último elemento, que es el máximo
    
    # Imprimir la lista sin el máximo valor
    print("Lista sin el máximo valor:", lista_sin_duplicados)
    
    # Retornar la lista sin el máximo valor
    return lista_sin_duplicados


    
    
def promedio(lista_sin_max):
    acum  = 0
    for numero in lista_sin_max:
        acum+=numero
    prom = acum/len(lista_sin_max)
    return prom