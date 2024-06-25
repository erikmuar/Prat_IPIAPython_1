# Proyecto dia 4 
from random import *

nombre = input("¿Cual es tu nombre? ")

print(f"Hola {nombre}, vas a tener que adivinar un numero entre el 1 y el 100 \n Tienes 8 intentos para adivinarlo")

intentos = 0

solucion = randint(1,100)


while intentos < 8: 
    numero = int(input("Introduce un número: "))
    intentos += 1
    
    if numero < 1 and numero > 100:     
        print("Este número no está permitido, vuelve a elegir otro.")
        
    elif numero < solucion: 
        print("El número elegido es menor a la solución, elige otro.")
       
        
    elif numero > solucion: 
        print("El número elegido es mayor a la solución, elige otro.")
        
        
    elif numero == solucion:
        print(f"Felicidades {nombre}, has acertado! El numero de intentos ha sido {intentos}")
        break
    
if numero != solucion:
    print(f"Se han acabado los intentos, el número era {solucion}")       






