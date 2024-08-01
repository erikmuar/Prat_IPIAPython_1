
cadena = "Hola"

for letra in cadena: 
    print(letra)
else:
    print("Fin de ciclo")

    
# Break
for letra in "Holanda": 
    if letra == "a":
        print(f"Letra encontrada: {letra}")
        break #Con la palabra reservada break se para de leer el codigo en esta linea 
else:
    print("Fin ciclo")
    

# Continue 

for i in range(6):
    if i%2 == 0: 
        print(f"Valor: {i}")
        
        
        
# Ejercicio 1 itera un rango de 0 a 10 e imprime los numeros divisibles entre 3.

for i in range(0,11,1):
    if i %3 == 0:
     print(i)
    

# Ejercicio 2 Crea un rango de numeros de 2 a 6 e imprimelos

for i in range(2,6):
    print(i)
    
# Ejercicio 3 Crea un rango de 3 a 10, pero con incremento de 2 en 2, en lugar de 1 en 1 

for i in range(3,10,2):
    print(i)