mi_tuple = (1,2,3,4)
print(type(mi_tuple))

mi_tuple = (1,2,3,4)

print(mi_tuple[-2])

mi_tuple[0]=6  # Da error porque las tuplas son inmutables por lo que no se pueden modificar 




#%%  


mi_tuple = (1,2,(10,20),4)

print(mi_tuple[2][0])
# %%

mi_tuple = (1,2,(10,20),4)

mi_tuple = list(mi_tuple)

mi_tuple = tuple(mi_tuple)

print(type(mi_tuple))

# %%

t = (1,2,3)

x,y,z = t

print(x,y,z) # Esto se puede hacer con listas, diccionarios y tuplas siempre que haya el mismo numero de elementos que de variables 


# %%

t = (1,2,3,1)

print(t.count(1)) #Sirve para contar cuantas veces aparece el numero entre parentesis en la lista o tupla

print(t.index(2)) # Para saber el indice del numero entre parentesis




