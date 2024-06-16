# Ejercicio 13
# Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.

def filtrar_palabras(lista:list,n:int):
    
    for largo in lista:
        posicion = lista.index(largo)
        if (len(largo) > n):
            print(largo)
        
            
   
filtrar_palabras(["nueve","dos","cuarenta","diecisiete","hola","jamones"],5)