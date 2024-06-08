# https://pythondiario.com/2013/05/ejercicios-en-python-parte-1.html
"""
  2 - Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
"""

# %% Extensión de la función calcular_maximo_dos del ej01:
def calcular_maximo_tres(a: int, b: int, c: int):
    if a > b and a > c: 
      return a 
    if b > a and b > c: 
      return b 
    if c > a and c > b: 
      return c

calcular_maximo_tres(1,4,9)


# %% Tests
r_1 = calcular_maximo_tres(1, 2, 3) # 3
assert r_1 == 3

# %% ¿Cómo se puede calcular el máximo o mínimo de una lista de números?
# Por simplicidad podemos suponer que son int
lista = [44,25,140,2,57,91]

resultado = max(lista)
print(resultado)


def calcular_maximo_lista(lista: list):

  maximo = lista[0]
  for i in lista:
    if i > maximo:
      maximo = i
  return maximo
  
lista = [1,3,5,3,9,14,5]
calcular_maximo_lista(lista) 
print("El resultado es ",calcular_maximo_lista(lista))

# %% 
# Encontrar minimo de una lista 

listo = [21,44,5,2,56,88]
minimo = min(listo)
print ( minimo)


def numero_minimo_lista(lista):
  if not lista:
    lista = None
    return ("No hay lista")
  
  numero = lista[0]
  for i in lista: 
    if i < numero:
      numero = i 
  return numero

conjunt = [20,10,6,42,82]
numero_minimo_lista(conjunt)
    
# %% Tests
lista = [-1, 0, 1] # max -> 1
res = calcular_maximo_lista(lista)
assert res == 1