# Juego ChoHan
import random

billetera = 10

ganado = 0
print("--- Bienvenido a Cho Han ---")
print(f"Usted tiene {billetera}$ en la billetera")


while billetera > 0:
    apuesta = int(input("Haga su apuesta: "))
    if apuesta <= billetera:
        dado1 = random.randint(1,6)
        dado2= random.randint(1,6)
        total = dado1 + dado2
        resto = total%2
        parimp = input("Adivina, ¿Es par o impar?")
        print(f"Salió {dado1} y {dado2} = {total} ")
    else:
        print("El dinero es mayor al que tiene en la billetera")
    
    
    
apuesta = int(input("Cuanto dinero deseas apostar?"))


