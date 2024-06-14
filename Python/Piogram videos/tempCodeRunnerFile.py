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
    
autoMas = max(contL)
posi = contL[autoMas] 
cocheMas = automotores[posi]
print(autoMas)    