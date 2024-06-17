#Escribir un pequeño programa donde:
#- Se ingresa el año en curso.
#- Se ingresa el nombre y el año de nacimiento de tres personas.
#- Se calcula cuántos años cumplirán durante el año en curso.
#- Se imprime en pantalla.

import datetime


def main():
    
    def calcular_edad(año_curso, año_nacimiento):
    
        año_curso = datetime.datetime.now().year
        edad = año_curso-año_nacimiento
        return edad

    año_actual = int(input("Ingresa que año es: "))
    
    año_curso = datetime.datetime.now().year
    
    personas = []
    
    for i in range(3):
        nombre = input(f"Introduce el nombre de la persona {i+1}: ")
        año_nacimiento = int(input(f"Introduce año de nacimiento de {nombre}: "))
        personas.append((nombre,año_nacimiento))
        
    for nombre, año_nacimiento in personas:
        edad = calcular_edad(año_curso, año_nacimiento)
        print(f"{nombre} cumplirá {edad} años en el año {año_curso}")
        
        

main() 