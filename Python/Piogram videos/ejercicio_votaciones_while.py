# Ejercicio votaciones 
# Desarrolla un programa que permita votar a cualquier persona de la lista poniendo solo el nombre al votar, considera que solo hay una fila para votar(Se vota de uno a uno), la votacion finaliza cuando se escriba la palabra "Fin" en vez de un nombre. 

# Cuando acaben las votaciones el programa debe mostrar los siguientes datos:
#    - El total de estudiantes que votaron
#    - El ganador 
#    - Votos del ganador

lista = ["Alejandro", "Pedro","Juan", "Carlos","Gabriela","Andrea","Maria","Carla",]

contadorVotos = [0]*len(lista)

voto = input("Introduce el nombre de la persona que quieras votar o introduce ""FIN"": ")

while voto != "FIN":
    votoMayus = voto.title()  # .title() es para que la primera letra de la palabra sea mayuscula
    if votoMayus in lista:   
        posicion = lista.index(voto)
        contadorVotos[posicion]+= 1

