opcion = ""

while opcion != 3:
    print("Bienvenido a tu calculadora")
    print("1.- Suma")
    print("2.- Resta")
    print("3.- Salir")
    opcion = int(input("Ingresa un numero"))
    if (opcion == 1):
        num1 = int(input("Introduce el primer numero: "))
        num2 = int(input("Introduce el segundo numero"))
        suma = num1 + num2
        print(f"La suma de los numeros es {suma}")
    elif (opcion == 2):
        num1 = int(input("Introduce el primer numero"))
        num2 = int(input("Introduce el segundo numero"))
        resta = num1 - num2
        print(f"La resta de los numeros es {resta}")
    elif(opcion == 3):
        print("Salir")
    else: 
        print("Ingresa el número de nuevo")