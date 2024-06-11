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
# Hacer una funcion en la que introduzcas una lista de numeros [4,7,8] y te devuelva la media y si has aprobado o no

def comprobar_nota(lista:list):
    sumatorio = 0
    for num in lista:
       sumatorio+=num
    promedio = sumatorio/len(lista)
    
    
    if promedio < 5:
        return (f"El promedio es {promedio}, por lo que ha suspendido")
    else: 
        return (f"El promedio es {promedio}, por lo que ha aprobado")
        
comprobar_nota([5.8,7.4,9.2,5.1,3.5,1.1])
# %%
