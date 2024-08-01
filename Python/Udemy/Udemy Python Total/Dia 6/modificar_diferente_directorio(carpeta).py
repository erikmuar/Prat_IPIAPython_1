import os 

ruta = os.getcwd() #Te dice la ruta de donde está el archivo 

print(ruta)

#%% cambiar la ruta del archivo 


ruta = os.chdir("C:\\Code\\Prat_IPIAPython_1\\Python\\Udemy Python Total\\Dia 6\\carpeta para hacer pruebas") #Hay que poner la ruta entre comillas y doble \\

archivo = open("cambio.txt")

print(archivo.read())


# %%

ruta = os.makedirs("C:\\Code\\Prat_IPIAPython_1\\Python\\Udemy Python Total\\Dia 6\\carpeta para hacer pruebas\\otra_mas") #Hay que poner la ruta entre comillas y doble \\

archivo = open("archivo.txt")

print(archivo.read())
# %%
