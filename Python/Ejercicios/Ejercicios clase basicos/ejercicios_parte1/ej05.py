# https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
"""
  5 - Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
  
  Por ejemplo: 
  - suma([1,2,3,4]) debería devolver 10 
  - y multiplicacion([1,2,3,4]) debería devolver 24.
"""



#%% suma
def suma(lista: list) -> int | float:
  acumul = 0
  for i in range(len(lista)):
   num = lista[i]
   acumul += num
  print(acumul)
  
suma([1,5,9,12,20])

assert suma([1,2,5,7,3]) == 18 



#%% multiplicacion
def multiplicacion(lista: list) -> int | float:
  acumul = 1 
  for i in range(len(lista)):
    num = lista[i]
    acumul *= num
  print(acumul)

multiplicacion([3,7,2,3])

#%% Tests
assert suma([1,2,3,4]) == 10
assert multiplicacion([1,2,3,4]) == 24
# %%
