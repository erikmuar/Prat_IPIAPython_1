# Ejercicio 12
# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.

def mas_larga(lista:list):
    
    word = lista[0]
    for palabra in lista:
        if (len(word) < len(palabra)): 
            word = palabra
    print(word)
        
mas_larga(["hola","califragilistico","diez", "melon"])