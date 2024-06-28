def reducir_lista(lista_numeros):
    
    lista_sin_duplicados = list(set(lista_numeros))
    
    print(lista_sin_duplicados)
    
    lista_ordenada = lista_sin_duplicados.sort()
    
    print(lista_ordenada)
    
    lista_sin_max = lista_ordenada.pop()
    
    print(lista_sin_max)
    
    return lista_sin_max

reducir_lista([2,4,6,15,6,5])