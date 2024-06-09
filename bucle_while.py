#Bucle while

# Ejemplo inicial

i = 9 
while i <= 13:
    print(i)
    i += 1
    
print("Fin")


# Ejercicio 1 
# Validación 
# Escribe un programa que permita el ingreso de un numero, si el usuario no ingresa un numero entonces vuelve a pedir que se ingrese otra vez


i = input("Ingresa un número")
while not i.isdigit():
    print("Tienes que introducir un número, vuelve a intentarlo")
    i = input("Ingresa un numero: ") 
    
print(f"Es el numero {i}")




# Ejercicio 2 

# Escribe un programa que permita al usuario el ingreso de n numeros. 
# Primero debe preguntar al usuario cuantos numeros desea ingresar. Al final del programa debe presentar la sumatoria de dichos números.
suma = 0 
numeros = int(input("Cuantos numeros deseas ingresar: "))
ciclo = 0 
while ciclo < numeros: 
   num = int(input("introduce un numero "))
   suma += num 
   ciclo +=1

print("La suma es", suma)    

# Ejercicio 3 
# Crear una calculadora con el siguiente menu 
# "Bienvenido a tu calculadora
# 1.- Suma
# 2.- Resta 
# 3.- Salir
# ingrese opcion "
#Pedir al usuario que opcion desea usar. Si pide la 1 o la 2, pide dos numeros y realiza la operacion. EL programa deberá seguir mostrando el menu hasta que el usuario coloque la opcion 3

#Inventada por mi 
calculadora = int(input("Bienvenido a tu calculadora 1.- Suma 2.- Resta 3.- Salir ingrese opcion" ))

while calculadora == 1 or calculadora == 2:
    num1 = int(input("Introduce el primer numero"))
    num2 = int(input("Introduce el segundo numero"))
    if calculadora == 1: 
        suma = num1 + num2 
        print(suma)
        calculadora = int(input("Bienvenido a tu calculadora 1.- Suma 2.- Resta 3.- Salir ingrese opcion" ))
        
    elif calculadora == 2:
        resta = num1 - num2 
        print(resta)
        calculadora = int(input("Bienvenido a tu calculadora 1.- Suma 2.- Resta 3.- Salir ingrese opcion" ))
        
    elif calculadora == 3: 
        print("Salir")
    
    else: 
        print("Ingresa una de las opciones")


# Solución

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