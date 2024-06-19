mi_lista = ["a","b","c"]

resultado = len(mi_lista)

print(resultado)

# Indexado

mi_lista = ["a","b","c"]

resultado = mi_lista[0]

print(resultado)

# Concatenacion 

mi_lista = ["a","b","c"]

mi_lista2 = ["d","e","f"]

print(mi_lista + mi_lista2)

# Para crear una lista con las dos

mi_lista3 = mi_lista + mi_lista2

#Cambiar un indice de la lista por otro string

mi_lista3[0] = "alfa"

print(mi_lista3)

#Append, o agregar un elemento a la lista

mi_lista3.append("g")

print(mi_lista3)

# Pop o eliminar un elemento de la lista

mi_lista3.pop()  # Si dejas el parentesis vacío interpreta que se elimina el ultimo elemento de la lista, por lo que se elimina la recien agregada "g"

# tambien podemos guardar el elemento eliminado en una variable 

eliminado = mi_lista3.pop(0)

print(eliminado)


# Sort para ordenar la lista, tambien ordena numeros 

lista = ["g","o","b","m","c"]

lista.sort()

print(lista)

# Reverse, lo mismo que sort pero al reves

lista = ["g","o","b","m","c"]

lista.sort()
lista.reverse()

print(lista)

