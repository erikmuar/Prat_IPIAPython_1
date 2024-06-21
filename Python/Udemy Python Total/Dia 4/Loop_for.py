lista = ["a","b","c"]

for letra in lista: 
    numero_letra = lista.index(letra) + 1 
    print(f"Letra {numero_letra}: {letra}")
    
    
lista2 = ["Laura","Pedro","Luis","Javier","Leandro"]

for nombre in lista2:
    nombre = nombre.lower()
    if nombre.startswith("l"):
        print(nombre)



dic = {"clave1":"a","clave2":"b","clave3":"c" }

for item in dic: 
    print(item)  # Se imprime solo la primera parte, las clave1, clave2 etc...

for item in dic.items(): 
    print(item) # Se imprime todo 
    
for item in dic.values():
    print(item) # Solo los valores de dentro


for a,b in dic.items(): 
    print(a,b) # Se imprime todo pero separado  


