# Tipo Valor 
#1. Vehiculo $ 3.50
#2. Camión $ 12.00 
#3. Tractomula $ 16.00
# Calcula el valor a pagar por cada automotor que pase por el peaje
# TOtal recaudado en el peaje al final de ese dia
# Total recaudado por cada tipo de automotor 
# Cual es el tipo de Automotor que mas transita por el peaje

automotores = ["Vehiculos", "Camiones","Tractomula"]
precios= [3.5,12.00,16.00]
contL= [0,0,0]
acumL = [0,0,0]
ingreso = int(input("Ingresa el numero del vehiculo: "))

while ingreso != 0: 
    if (ingreso<=len(automotores)):
        precio = precios[ingreso-1]
        print("Debe pagar: ",precio)
        contL[ingreso-1]+=1
        acumL[ingreso-1]+=precio 
    else: 
        print("Error de ingreso")
        
    ingreso = int(input("Ingresa el numero del vehiculo: "))
    print("Total por cada tipo de automotor: ")
for i in range(len(automotores)):
    autos=automotores[i]
    acum = acumL[i]
    print(autos,":",acum)
    
maxi= max(contL)  
posi = contL.index(maxi)
autoMax = automotores[posi]
print("El automotor que mas transita por el peaje es: ", autoMax)

totalDia = sum(acumL)
print(totalDia)
