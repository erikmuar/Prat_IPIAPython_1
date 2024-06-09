#Ejercicio 1 

# Escribe un programa que pregunte cuantos números se van a introducir, permite el ingreso de dichos numeros y muestra por pantalla cuantos números son pares y la suma de todos los impartes
veces = int(input("Cuantos números deseas ingresar: "))
cont = 0 # EL contador se crea fuera y no dentro del for para que cuando acabe la primera iteracion no se resetee el valor de cont. SI no quieres que se resetee, crear fuera, si el ejercicio necesita que resetee crear dentro
acumulado = 0
for i in range(veces): 
    print("---Ciclo" + str(i+1)+"---")
    num = int(input("Ingrese un numero: ")) 
    if (num%2 == 0):
        cont += 1 # cont = cont+1 
        print(cont)
    else:
        acumulado+=num
print("La cantidad de numeros pares es: ",cont) #EL print va fuera de la funcion porque queremos solo el total una vez, si fuera dentro, nos imprimiria la suma y cont de cada iteracion
print("La suma total de numeros impares es: ",acumulado)


