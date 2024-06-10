# 6 - Definir una función inversa() que calcule la inversión de una cadena. Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

def inversa(string:str):
    
    palabra = string
    
    inverted = palabra[::-1]
    
    print(inverted)
    
inversa("hola como va")