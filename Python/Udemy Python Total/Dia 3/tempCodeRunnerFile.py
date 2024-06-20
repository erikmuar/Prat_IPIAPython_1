texto = input("Ingresa un texto: ").lower()
letra1 = input("Ingresa la primera letra: ").lower()
letra2 = input("Ingresa la segunda letra: ").lower()
letra3 = input("Ingresa la tercera letra: ").lower()

lista = [letra1,letra2,letra3]

contad1 = texto.count(letra1)
contad2 = texto.count(letra2)
contad3 = texto.count(letra3)

print(texto.count(letra1))
print(texto.count(letra2))
print(texto.count(letra3))


lista_palabras = texto.split()
largo = len(lista_palabras)

print(largo)

primera_letra = texto[0]
ultima_letra = texto[-1]

print(primera_letra,ultima_letra)

orden_inverso = lista_palabras.reverse()

print(orden_inverso)