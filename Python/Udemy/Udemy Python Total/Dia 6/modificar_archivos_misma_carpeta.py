# Abrir archivos e imprimir lineas 
#%%


mi_archivo = open("Prueba.txt")

print(mi_archivo.readline())


una_linea = mi_archivo.readline()  # si ponemos esto otra vez sale la segunda linea y asi sucesivamente

print(una_linea)


mi_archivo.close()

#%% 


archivo = open("prueba1.txt", "r") # La r es solo para leer el archivo sin poder modificarlo
 
archivo.write("Soy el nuevo texto")
 
print("prueba1.txt")
 
archivo.close()


# %%
archivo = open("prueba1.txt", "w") # La w es para sobreescribir lo que hay en el archivo o para crear uno nuevo.
 
# archivo.write("Soy el nuevo texto") # Puedes escribir un bloque de texto con tres comillas """  """  para poner espacios

lista = ["hola","mundo","aqui","estoy"]

for p in lista: 
   print(archivo.writelines(p + "\n"))
    

 
archivo.close()

#%% 

archivo = open("prueba.txt", "a") # La a te permite seguir escribiendo en un archivo ya empezado sin borrarlo.
 
archivo.write(" \n Bienvenido")
 
 
 
archivo.close()

# %%
mi_archivo = open("prueba2.txt","w")

mi_archivo.write("Nueva cosa")
 
print(mi_archivo)
# %%

archivo = open("prueba.txt", "w")

print(archivo.write("Cambio de texto"))



archivo.close()
# %%
