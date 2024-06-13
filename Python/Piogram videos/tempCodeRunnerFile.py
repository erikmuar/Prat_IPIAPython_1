# solo divisible para si mismo y para 1 

numero = int(input("Escribe un numero: "))


if numero > 1: 
    for i in range(2, numero):
        resto = numero%i 
        print(f"{numero} % {i} = {resto}")

else:
    print(f"El numero{numero} no es valido")

    