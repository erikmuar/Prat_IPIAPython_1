# Crea un programa que simule el juego del ahorcado, su programa debe seleccionar una palabra aleatoria de una lista de palabras, ejemplo si la palabra es "POLLOS" entonces muestre una pista "P____S"
#EL usuario debe ingresar y si es igual a la palabra aleatoria entonces el programa muestra True, en caso contrario False.

import random as rd
palabras = ["Madserker","Melon","Hola","Python","jueves"]
indice = rd.randint(0,len(palabras) - 1) # Desde 0 que es la primera posicion de la lista hasta el len -1 porque va de 0 a 4 no a 5 
pal = palabras[indice]
palMayus= pal.upper()
letraPri = palMayus[0] 
letraUlt= palMayus[-1]
n = " _ "*(len(palMayus)-2)
print(letraPri, n, letraUlt)

palUser = input("Adivine la palabra").upper



#%%

import random as rd 

palabras = ["Madserker","Melon","Hola","Python","jueves"]



indice = rd.randint(0,len(palabras)-1)
palab = palabras[indice]
palabMayus = palab.upper()
letraPri = palabMayus[0]
letraUlt= palabMayus[-1]
n = " _ "* (len(palabMayus)-2)
print(letraPri, n, letraUlt)


palUser = input("Adivina la palabra")

if palUser == palabMayus:
    print("Win") 


# %%
