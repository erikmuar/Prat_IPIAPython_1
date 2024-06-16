def filtrar_palabras(lista:list,n:int):
    
    for largo in lista:
        posicion = lista.index(largo)
        if (len(largo) <= n):
            del lista[posicion]
        else:
            print(largo)
            
    
    
   
filtrar_palabras(["nueve","dos","cuarenta","diecisiete","hola","jamones"],8)