# Crea un programa que simule el juego del ahorcado, su programa debe seleccionar una palabra aleatoria de una lista de palabras, ejemplo si la palabra es "POLLOS" entonces muestre una pista "P____S"
#EL usuario debe ingresar y si es igual a la palabra aleatoria entonces el programa muestra True, en caso contrario False.

import random as rd
palabras = ["Madserker","Melon","Hola","Python","jueves"]
num = len(palabras)
indice = rd.randint(0,num - 1) # Desde 0 que es la primera posicion de la lista hasta el len -1 porque va de 0 a 4 no a 5 
pal = palabras[indice]
palMayus= pal.upper()
letraPri = palMayus[0] 

