"""
    1 - Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.
    """
    # %% 
 
# Consideramos que a y b son int 

def calcular_maximo(a: int,b: int)-> int:
    
    """
    Fn que calcula máxima 
    {param } a: int 
    {param  }b: int
    
    """
    if a > b:
            return a 
    else: 
           return b 
# %%
calcular_maximo(1,2)
# %%
def calcular_maximo(a: int,b: int)-> int:
    
    """
    Fn que calcula máxima 
    {param } a: int 
    {param  }b: int
    
    """
    if a > b:
            return a 
    else: 
           return b 
       
r_1 = calcular_maximo(1,3) # 3
r_2 = calcular_maximo("1","2") # '2'
r_3 = calcular_maximo(5,5) # 3

assert r_1 == 3
assert r_2 == "2"
assert r_3 == 5

# %%
