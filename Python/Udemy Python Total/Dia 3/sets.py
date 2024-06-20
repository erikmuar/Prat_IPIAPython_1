# Los elementos dentro de set son inmutables, no tienen un orden interno y son elementos unicos, no se pueden repetir, python elimina los repetidos


mi_set = set([1,2,3,4,5])

print(type(mi_set))

print(mi_set)


otro_set = {1,2,3}

print(type(otro_set))

print(otro_set)


print(2 in mi_set)

# Unión de sets 

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)

#%%
# Add o agregar

s1 = {1,2,3}

s1.add(4)

print(s1)
# %%

# Remove o eliminar

s1 = {1,2,3}

s1.remove(3)

print(s1)

# Si intentamos eliminar un elemento que no esta da error
# %%

# Discard o descartar es lo mismo que remove pero al hacerlo con un elemento que no existe no da error

#%% 

#Pop tambien elimina pero como no hay orden elimina un numero aleatorio 

#%% 

# #Clear, deja vacio el set

s1 = {1,2,3}

s1.clear()

print(s1)
# %%
