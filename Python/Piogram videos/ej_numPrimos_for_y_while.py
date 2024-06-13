# Crea un programa que permita identificar si un numero es primo o no.
# Numero primo : 
# Un número natural(Entero y positivo)
# Mayor de 1 
# solo divisible para si mismo y para 1 

numero = int(input("Escribe un numero: "))


if numero > 1: 
    for i in range(2, numero):
        resto = numero%i 
        print(f"{numero} % {i} = {resto}")
        
        if resto 

else:
    print(f"El numero{numero} no es valido")

    