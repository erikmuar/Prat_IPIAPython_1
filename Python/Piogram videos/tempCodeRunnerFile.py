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
      
    
        
 
    