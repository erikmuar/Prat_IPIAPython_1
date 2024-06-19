# INDEX



mi_texto = "Esta es una prueba"
resultado = mi_texto.index("e",6)
print(resultado)


# Slicing

# De un indice a otro

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)


# De un indice hasta el final o desde el inicio hasta un indice

texto = "ABCDEFGHIJKLM"
fragmento = texto[2:]
print(fragmento)


texto = "ABCDEFGHIJKLM"
fragmento = texto[:5]
print(fragmento)

# De inicio a fin saltando de dos en dos

texto = "ABCDEFGHIJKLM"
fragmento = texto[::2]
print(fragmento)


#Para imprimir toda la frase del reves 

texto = "ABCDEFGHIJKLM"

fragmento = texto[::-1]
print(fragmento)



