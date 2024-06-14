<<<<<<< HEAD
# Juego Cho Han
import random

billetera = 10
ganado = 0
continuar = "Si"
print("--- Bienvenido a Cho Han ---")
print(f"Tiene {billetera}$ en la billetera")

apuesta = int(input("Haga su apuesta: "))

while billetera > 0 and continuar == "Si":
   
    if apuesta <= billetera:
        dado1 = random.randint(1,6)
        dado2= random.randint(1,6)
        total = dado1 + dado2
        resto = total%2
        parimp = input("Adivina, ¿Es par o impar?")
        print(f"Salió {dado1} y {dado2} = {total} ")
        
        if resto == 0 and parimp == "par":
            billetera += apuesta
            ganado+=1 
            print("Has ganado!")
        elif resto !=0 and parimp == "impar":
            billetera+=apuesta
            ganado+=1
            print("Has ganado!")
        else: 
            billetera-=apuesta 
            print("Has perdido!")
        print(f"Dinero restante en la billetera es: {billetera}")
        
        if billetera != 0:
            continuar = input("¿Deseas continuar? Si o No  ")
            apuesta = int(input("Haga su apuesta: "))            
            
        
    else:
        print("El dinero es mayor al que tiene en la billetera")
    
print(f"Has ganado {ganado} partidas")
print("Gracias por jugar.")
=======
for num in range(1,100):
    if num > 1: 

        contador = 0 

        i = 2

        while i < num and contador == 0: 
            resto = num%i
            
            if resto == 0:
                contador+=1
            i +=1 
        if contador == 0:
            print(num)  
      
    
        
 
    
>>>>>>> 9e6496c448088759bd490591539f3729eda104b7
