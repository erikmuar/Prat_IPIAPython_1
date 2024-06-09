veces = int(input("Cuantos números deseas ingresar: "))

for i in range(veces): 
    acumulado = 0 
    num = int(input("Ingrese un numero: "))
    if (num%2 == 0):
        print(num)
    elif(num%2 == 1):
        acumulado+=num
    
print("La suma de los impares es: ", acumulado)