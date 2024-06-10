# Crea un programa que pida al usuario la cantidad de segundos y muestre cuantas horas minutos y segundos son


segundos = int(input("Ingresa la cantidad de segundos: ")) # 3665

horas =  segundos // 3600 # Esto da el número de horas = 1

resto1 = segundos%3600 # Aquí calculamos el resto de la operación de arriba, de las horas = 65


minutos = resto1 // 60  # Obtenemos el número de minutos 

resto2 = resto1%60



print("EL total de horas es: ",horas)
print(resto1)
print(minutos)
print(resto2)