# Escribe un programa que permita el ingreso de dos numeros y muestre por pantalla True si el primer numero es divisible para el segundo, en caso contrario que devuelva False.


num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))



if (num1%num2 == 0 ):
    print(f"¿Es {num1} divisible de {num2} ? True")
else: 
    print(f"¿Es {num1} divisible de {num2} ? False")
    


#%% Otra forma de hacerlo sin if 


num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

residuo = num1 % num2 

condicion = residuo == 0

print(f"{num1} es divisible de {num2}? {condicion}")
# %%
