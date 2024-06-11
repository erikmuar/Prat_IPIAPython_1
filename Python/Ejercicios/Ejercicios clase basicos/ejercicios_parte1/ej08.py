# 8 - Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.
# %%

def superposicion(lista1: list, lista2:list):
    for i in lista1: 
        x = lista1[i]
        if x in lista2:
            return True
        else: 
            return False
    

superposicion([1,5,8,22,90],[2,7,5,40,61])
# %%
