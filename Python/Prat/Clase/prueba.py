# %% 

print("Hola")
a = 100
b = 50 
print(1+1)
# %% 

n = int(input("Introduce un numero: "))
for i in range(10):
    resultado = i * n

# %%

numero = int(input("Introduce un numero"))

for i in range(3,10):
    
    resul = i * numero
    print(f"La multiplicacion {i} * {numero} = {resul}")
# %%

for numero in range(1,10):
    print("--- Tabla del",str(numero),"---")
    for i in range(1,10):
        resultado = i*numero
        print(numero," x",i,"=",resultado)