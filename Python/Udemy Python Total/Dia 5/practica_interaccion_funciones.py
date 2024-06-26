from random import randint

# Función que lanza dos dados y devuelve sus valores
def lanzar_dados():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)
    return dado1, dado2

# Función que evalúa la jugada en base a la suma de los valores de los dados
def evaluar_jugada(dado1, dado2):
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

# Llamar a la función lanzar_dados para obtener los resultados de los dados
dado1, dado2 = lanzar_dados()

# Evaluar la jugada con los resultados obtenidos
resultado = evaluar_jugada(dado1, dado2)

# Imprimir el resultado
print(resultado)
