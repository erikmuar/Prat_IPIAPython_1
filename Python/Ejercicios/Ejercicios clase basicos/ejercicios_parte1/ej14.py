# Ejercicio 4
# Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.

palabra = input("Introduce la palabra: ")

def ingreso_cadena(palabra:str):
    
    contador = 0 
    for i in range(len(palabra)):
       letra = palabra[i]
       if letra.isupper():
           contador+=1
    print(f"El numero de letras mayúsculas es: {contador}")
    
    
ingreso_cadena(palabra)