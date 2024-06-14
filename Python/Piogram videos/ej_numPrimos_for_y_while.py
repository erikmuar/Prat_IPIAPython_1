# Crea un programa que permita identificar si un numero es primo o no.
# Numero primo : 
# Un número natural(Entero y positivo)
# Mayor de 1 
# solo divisible para si mismo y para 1 

numero = int(input("Escribe un numero: "))


if numero > 1: 
    
    cont= 0 
    
    for i in range(2, numero):
        resto = numero%i 
        print(f"{numero} % {i} = {resto}")
        
        if resto == 0: 
           cont +=1 
           
    if cont== 0: 
        print(f"{numero} es primo")
    else:
         print(f"{numero} no es primo")
    
        
            

else:
    print(f"El numero{numero} no es valido")




# Lo mismo pero con while 

num = int(input("Introduce un numero: "))


if num > 1: 

    contador = 0 

    i = 2

    while i < num and contador == 0: 
        resto = num%i
        if resto == 0:
            contador+=1
        i +=1 
    if contador == 0:
        print(f"El numero {num} es primo")
    else:
        print(f"el numero {num} no es primo")
        
else: 
    print(f"el numero {num} no es primo")
    
    
    
    
#Para sacar los numeros primos de una lista



for num in range(1,100):
    if num > 1: 

        contador = 0 

        i = 2

        while i < num and contador == 0: 
            resto = num%i
            
            if resto == 0:
                contador+=1
            i +=1 
            
        if contador == 0:
            print(num)  
      
    
        
 
    