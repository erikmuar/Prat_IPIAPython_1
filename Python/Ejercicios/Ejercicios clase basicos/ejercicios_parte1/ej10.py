# 10 - Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla. Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
# ****
#*********
#*******
#%%
def procedimiento(lista:list):
    for i in range(len(lista)):
        posicion = lista[i]
        print(posicion*"*")
        
procedimiento([2,4,6])

# %%
#%%
def procedimiento(lista:list):
    for i in lista:
        print(i*"*")
        
procedimiento([4,11,9])
# %%
