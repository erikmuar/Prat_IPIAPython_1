#Las tuplas son lo mismo que las listas pero las tuplas son inmutables, no se puede borrar ni añadir nada.

#Ejercicio Crea una lista que solo incluya los numeros menores a 5 

tupla = (13, 1, 3, 6, 8, 2, 5 ,8)

lista = []
for i in tupla:
    if i < 5:
        lista.append(i)
print(lista)

# la primera parte es key y la segunda value

coche = {
    
    "marca":"Volvo",
    "cv" : "200",
    "modelo": "v80",
}

print(coche)


#acceder a un elemento (key)

print(coche["marca"])