# Mayuscula

texto = "Este es el texto de Federico"

resultado = texto[2].upper()

print(resultado)

# Minúscula 

texto = "Este es el texto de Federico"

resultado = texto.lower()

print(resultado)

# Split 

texto = "Este es el texto de Federico"

resultado = texto.split()   # En este caso se utilizan los espacios para separar cada palabra

print(resultado)


texto = "Este es el texto de Federico"

resultado = texto.split("t")   # Aqui se usa cada letra "t" para marcar la separación

print(resultado)

# Join

a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) # e es un " " (espacio) porque al hacer join de varios objetos, se pone e entre medio de cada uno

print(e)


# Find 

texto = "Este es el texto de Federico"

resultado = texto.find("s")   

print(resultado)


#Replace

texto = "Este es el texto de Federico"

resultado = texto.replace("Federico","todos")   # La primera palabra es la palabra que se va a reemplazar y la segunda es por cual la reemplazas

print(resultado)