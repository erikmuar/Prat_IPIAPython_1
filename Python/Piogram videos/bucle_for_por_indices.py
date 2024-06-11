# Bucle for por indices 

frutas = ["Mora","Fresa","Sandia","Piña","Uva"]

precioxlb = [0.5, 1.00, 1.55, 1.20, 2.00]

# Imprime solo las frutas que tengan un valor por debajo de 1.50

for i in range(len(frutas)): # La i recorre y se convierte en el rango de 0 a 4 que es el largo de la variable frutas, por lo que i es 0, luego 1, luego 2 etc, esto lo hace porque le decimos que tiene que recorrer el rango que es el largo de la lista de frutas(range(len(frutas)))
    fruta = frutas[i]
    precio = precioxlb[i]
    if precio < 1.50: 
        print(fruta)
        

frutas = ["Mora","Fresa","Sandia","Piña","Uva"]
precioxlb = [0.5, 1.00, 1.55, 1.20, 2.00]

for fruta in frutas: # Creamos la variable fruta para que sea cada valor de la lista en cada iteracion, en la primera iteración, fruta es Mora, en la segunda es Fresa, etc
    posicion = frutas.index(fruta) # Buscamos la posición mirando donde esta fruta(Mora en la primera iteracion) basandonos en el indice de la lista frutas, esto da posicion 0
    precio = precioxlb[posicion]# Se asigna el precio basandonos en la posicion de la fruta
    if precio < 1.5:
        print(fruta)

#%% 

#Imprime en pantalla todas las personas que compraron mora y la cantidad
frutas = ["Mora","Fresa","Mora","Piña","Uva"]
cantidad= [  5   , 10   ,  3   ,  5  ,  10 ]
clientes = ["Axell", "Zarinna","Luis", "Joel", "Kevin"]


for i in range(len(frutas)): 
    
    fruta = frutas[i]
    
    if fruta == "Mora":
        personas = clientes[i]
        cuantas = cantidad[i]
        print(personas,cuantas)



# %%

#Imprimir las frutas que valen 1.5 o mas 
frutas = ["Mora","Fresa","Sandia","Piña","Uva"]

precioxlb = [0.5, 1.00, 1.55, 1.20, 2.00]

for i in range(len(frutas)):
    
    precio =precioxlb[i]
    
    if precio >= 1.5:
        fruta = frutas[i]
        print(fruta)
        

#%% 

# Los strings tambien tienen indices 

palabra = "Madserker Melón"

for i in range(len(palabra)):
    letra = palabra[i]
    
    print(letra)
    
    
#%% 
frutas = ["Mora","Fresa","Sandia","Piña","Uva"]
for fruta in range(len(frutas)): # Creamos la variable fruta para que sea cada valor de la lista en cada iteracion, en la primera iteración, fruta es Mora, en la segunda es Fresa, etc
    print(fruta)
# %%
